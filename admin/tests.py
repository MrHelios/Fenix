from django.test import TestCase
from django.contrib.auth.models import User

class AdminTest(TestCase):

    def test_login_GET(self):
        r = self.client.get('/admin/login')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get('Content-type'), 'text/html; charset=utf-8')

    def test_login_template(self):
        r = self.client.get('/admin/login')
        self.assertTemplateUsed(r, 'login_admin.html')

    def test_login_superuser_POST_sucess(self):
        password = 'holaholahola'
        u = User.objects.create_superuser('hola','hola@hola.com', password)
        r = self.client.post('/admin/login', data={'admin':u.username, 'password': password})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/admin/subir')

    def test_login_superuser_POST_fail(self):
        password = 'holaholahola'
        u = User.objects.create(username='hola',password=password)
        r = self.client.post('/admin/login', data={'admin':u.username, 'password': password})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/admin/login')

    def test_logout_superuser_sucess(self):
        password = 'holaholahola'
        u = User.objects.create_superuser('hola','hola@hola.com', password)
        self.client.login(username=u.username, password=password)
        r = self.client.get('/admin/logout')
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/')

    def test_logout_superuser_fail(self):
        password = 'holaholahola'
        u = User.objects.create(username='hola',password=password)
        self.client.login(username=u.username, password=password)
        r = self.client.get('/admin/logout')
        self.assertEqual(r.status_code, 404)

    def test_subir_GET_sucess(self):
        password = 'holaholahola'
        u = User.objects.create_superuser('hola','hola@hola.com', password)
        self.client.login(username=u.username, password=password)
        r = self.client.get('/admin/subir')
        self.assertEqual(r.status_code, 200)

    def test_subir_GET_fail(self):
        password = 'holaholahola'
        u = User.objects.create(username='hola', password=password)
        self.client.login(username=u.username, password=password)
        r = self.client.get('/admin/subir')
        self.assertEqual(r.status_code, 404)

    def test_subir_GET_sucess_template(self):
        password = 'holaholahola'
        u = User.objects.create_superuser('hola','hola@hola.com', password)
        self.client.login(username=u.username, password=password)
        r = self.client.get('/admin/subir')
        self.assertTemplateUsed(r, 'subir.html')
