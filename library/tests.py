from django.test import TestCase
from library.models import Loan, Book, Member, Author
from django.contrib.auth import get_user_model
from datetime import date, timedelta

# Create your tests here.
class TestLoad(TestCase):
    def test_due_date_set(self):
        author = Author.objects.create(first_name="asdadas", last_name='asdas')
        book = Book.objects.create(title="sdaasdsad", 
                                   isbn='asdadsada',
                                   genre='Biography', available_copies=10, author=author)
        User = get_user_model()
        user = User.objects.create(username='asddsa', password='asdadasd')
        member = Member.objects.create(user=user)

        loan = Loan.objects.create(
            book=book,
            member=member
        )
        add_14_days = date.today() + timedelta(days=14)
        self.assertEquals(loan.due_date, add_14_days)
        pev_date = date.today() + timedelta(days=-1)
        loan = Loan.objects.create(
            book=book,
            member=member,
            loan_date=pev_date
        )
        self.assertEquals(loan.due_date, pev_date  + timedelta(days=14))