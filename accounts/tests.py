from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import SignupView


class SignUpTest(TestCase):

    def test_sign_up_url_resolves_to_sign_up(self):
        found = resolve('/accounts/signup')
        self.assertEqual(found.func, SignupView.as_view())

    def test_signed_in(self):
        ''' Want to make signup auto log in user
        Test is here but couldnt get to it in time.

        '''
        self.assert(request.user.is_authenticated)

