from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Your Order has been placed, Number {}'.format(order.id)
    message = 'Dear {},\n\n You have successfully placed an order. Your order id is {}'.format(order.Fname ,order.id)

    mail_sent = send_mail(subject, message, 'mmgerber@cableone.net', [order.email])

    return mail_sent
