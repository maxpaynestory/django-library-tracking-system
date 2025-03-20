from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from django.core.mail import send_mail

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_book_loans():
    today = date.today()
    overdue_loans = Loan.objects.filter(is_returned=False, due_date__gte=today).all()

    if overdue_loans.exists():
        for loan in overdue_loans:
            send_mail(
                "Reminder for overdue book load",
                "Your loan is overdue from 14 days. Please pay your loan as soon as possible",
                "from@example.com",
                ["to@example.com"],
                fail_silently=False,
            )
