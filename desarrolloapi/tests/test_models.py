from django.test import TestCase
from desarrolloapi.models import Contacto

class ContactoModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ContactoModelTest, cls).setUpClass()
        cls.testContacto = Contacto(nombre="Maxi", apellido="Manrique", email="prueba@prueba.com", direccion='prueba Santiago Chile', preferencia="Brasil")
        cls.testContacto.save()

    def testContactoToStringEmail(self):
        self.assertEquals(self.testContacto.email, "prueba@prueba.com")

    def testGetById(self):
        self.assertEquals(Contacto.getById(1), self.testContacto)

    def testShortName(self):
        self.assertEquals(self.testContacto.nombre, "Maxi")