import unittest

from metadatos.recibo import ReciboNomina


class ModuloTest(unittest.TestCase):

    def test_metadatos_recibos(self):
        reci = ReciboNomina()
        self.assertEqual(ReciboNomina.buscar_datos())