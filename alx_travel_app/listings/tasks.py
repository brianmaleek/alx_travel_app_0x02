from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(booking_id, user_email):
    """
    Task to send a payment confirmation email.
    """
    send_mail(
        subject='Payment Successful - Booking Confirmation',
        message=f'Your booking with ID {booking_id} has been confirmed and is successful.',
        from_email=None,
        recipient_list=[user_email],
        fail_silently=False
    )