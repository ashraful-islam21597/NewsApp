from django.test import TestCase
from django.test import TestCase
from django.urls import reverse

from .models import merchants, Order


class PostModelTest(TestCase):
    def setUp(self):
        merchants.objects.create(name='x',merchant_id=1)
        Order.objects.create(merchant_id=1,weight=2,Division="Dhaka",District="Dhaka",Street="Mohammadpur",Product_type="liquid",merchant_invoice_id=111001,Charge=60,
                             Cod_charge_add=0,return_charge_add=0)

    def test_merchant_content(self):
        m = merchants.objects.get(id=1)
        expected_object_name = f'{m.name}'
        self.assertEqual(expected_object_name,'x')
    def test_order_content(self):
        o = merchants.objects.get(id=1)
        expected_object_name = f'{o.name}'
        self.assertEqual(expected_object_name,'x')

class indexTest(TestCase):
    def setUp(self):
        merchants.objects.create(name='y',merchant_id=2)
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('create_order'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('create_order'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
    def test_view_uses_correct_template2(self):
        resp = self.client.get(reverse('orderlist'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'create_order.html')

class OrderListTest(TestCase):
    def setUp(self):
        merchants.objects.create(name='z',merchant_id=3)
    def test_view_url_about_location(self):
        resp=self.client.get('/orderlist/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_about_name(self):
        resp=self.client.get(reverse('orderlist'))
        self.assertEqual(resp.status_code, 200)
    def test_view_url_about_template(self):
        resp=self.client.get(reverse('orderlist'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'create_order.html')
