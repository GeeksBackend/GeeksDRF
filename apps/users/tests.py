from django.test import TestCase

from apps.users.models import User

# Create your tests here.
class UserTestCase(TestCase):
    def test_register_user(self):
        user = User.objects.create(username='test', email='test@gmail.com')
        user.set_password('geeksstudents')
        user.save()