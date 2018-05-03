from django.test import TestCase
from noticias.models import Noticia

class NoticiaPageTest(TestCase):

    def test_ultimas_noticias_templates(self):
        r = self.client.get('/noticias')
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'ultimas_noticias.html')

    def test_noticia_id_200(self):
        n = Noticia.objects.create()
        r = self.client.get('/noticias/%d/' % (n.id,))
        self.assertEqual(r.status_code, 200)

    def test_noticia_id_200(self):
        r = self.client.get('/noticias/99999/')
        self.assertEqual(r.status_code, 404)

    def test_noticia_id_templates_200(self):
        n = Noticia.objects.create()
        r = self.client.get('/noticias/%d/' % (n.id,))
        self.assertTemplateUsed(r, 'noticia_id.html')

    '''
    Agregar un template para error 404:
    
    def test_noticia_id_template_404(self):
        r = self.client.get('/noticias/1/')
        self.assertEqual(r.content, '')
    '''

class NoticiaModelTest(TestCase):

    def test_crear_noticia(self):
        n = Noticia()
        self.assertEqual(n.titulo, '')
        self.assertEqual(n.descripcion, '')
        self.assertEqual(n.text, '')
        self.assertNotEqual(n.fecha, '')
