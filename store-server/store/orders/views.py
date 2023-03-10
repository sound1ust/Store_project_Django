import uuid
from http import HTTPStatus

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from yookassa import Configuration, Payment

from common.views import TitleMixin
from orders.forms import OrderForm
from orders.models import Order
from products.models import Basket

Configuration.account_id = settings.SHOP_ID
Configuration.secret_key = settings.YOOMONEY_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Спасибо за заказ'


class CancelTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/cancel.html'
    title = 'Заказ отменен'


class OrderListView(TitleMixin, ListView):
    template_name = 'orders/orders.html'
    title = 'Заказы'
    queryset = Order.objects.all()
    ordering = ('-created')

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class OrderDetailedView(DetailView):
    template_name = 'orders/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailedView, self).get_context_data(**kwargs)
        context['title'] = f'Заказ №{self.object.id}'
        return context


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    title = 'Оформление заказа'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)

        baskets = Basket.objects.filter(user=request.user)
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
            "amount": {
                "value": baskets.total_sum(),
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": '{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success'))
            },
            "capture": True,
            "description": f'Заказ №{self.object.id}'
        }, idempotence_key)

        Order.objects.get(id=self.object.id).update_after_payment()
        return HttpResponseRedirect(payment.confirmation.confirmation_url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
