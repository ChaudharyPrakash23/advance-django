from django.test import TestCase
from youtube.admin import YouTubeUserAdmin, clear_users_cache


class YouTubeUserAdminTests(TestCase):
    def test_custom_cache_action_is_registered(self):
        self.assertIn(clear_users_cache, YouTubeUserAdmin.actions)
