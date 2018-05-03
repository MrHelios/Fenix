from django.test import TestCase

class HomeTest(TestCase):

    def test_home_page_templates(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'home.html')
