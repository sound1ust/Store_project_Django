import uuid
from yookassa import Configuration, Payment

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from http import HTTPStatus
from orders.forms import OrderForm

from common.views import TitleMixin


Configuration.account_id = settings.SHOP_ID
Configuration.secret_key = settings.YOOMONEY_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Спасибо за заказ'


class CancelTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/cancel.html'
    title = 'Заказ отменен'


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    title = 'Оформление заказа'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
            "amount": {
                "value": "100.00",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": '{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success'))
            },
            "capture": True,
            "description": "Заказ №1"
        }, idempotence_key)
        return HttpResponseRedirect(payment.confirmation.confirmation_url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
