from django.test import TestCase
from django .contrib.auth import get_user_model
from .models import Snack

class blog_tests(TestCase):
    @classmethod
    def set_up_data(cls):
        testuser1 = get_user_model().objects.create_user(username = 'testuser1',password = 'password')
        testuser1.save()

        test_snack = Snack.objects.create(

            purchaser = testuser1,
            name = "KitKat",
            description = "Red covered chocolate",
        )
        test_snack.save()

    def test_blog_content(self):
        snack = Snack.objects.get(id=1)
        self.assertEqual(str(snack.purchaser),"testuser1")
        self.assertEqual(str(snack.name),"KitKat")
        self.assertEqual(str(snack.description),"Red covered chocolate")


