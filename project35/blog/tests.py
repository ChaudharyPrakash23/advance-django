from django.test import TestCase

from blog.admin import UserProfileAdmin


class UserProfileAdminTests(TestCase):
    def test_admin_list_display_includes_name_email_and_sub(self):
        self.assertEqual(UserProfileAdmin.list_display, ('name', 'email', 'sub'))
