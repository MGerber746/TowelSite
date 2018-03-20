from django.test import TestCase

# Create your tests here.
class CollectionTest(TestCase):
    def test_base(self):
        r = self.client.get('/')
        self.assertEquals(r.status_code, 200)

    def test_about(self):
        r = self.client.get('/about/')
        self.assertEquals(r.status_code, 200)

    def test_products(self):
        r = self.client.get('/products/')
        self.assertEquals(r.status_code, 200)
