from django.test import TestCase

class JuegoPageTest(TestCase):

    def test_juego1_page(self):
        r = self.client.get('/g/juego1')
        self.assertEqual(r.status_code, 404)

    def test_juego1_page(self):
        r = self.client.get('/g/juego1/download')
        self.assertEqual(r.status_code, 404)
