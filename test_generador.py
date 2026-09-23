import string
import unittest

from generador import generar_contrasena


class TestGenerador(unittest.TestCase):
    def test_longitud_por_defecto(self):
        self.assertEqual(len(generar_contrasena()), 20)

    def test_longitud_y_tipos_de_caracteres(self):
        contrasena = generar_contrasena(20)

        self.assertEqual(len(contrasena), 20)
        self.assertTrue(any(c in string.ascii_lowercase for c in contrasena))
        self.assertTrue(any(c in string.ascii_uppercase for c in contrasena))
        self.assertTrue(any(c in string.digits for c in contrasena))
        self.assertTrue(any(c in string.punctuation for c in contrasena))
        self.assertTrue(
            all(
                c in string.ascii_letters + string.digits + string.punctuation
                for c in contrasena
            )
        )

    def test_rechaza_longitudes_fuera_del_rango(self):
        for longitud in (11, 129):
            with self.subTest(longitud=longitud):
                with self.assertRaises(ValueError):
                    generar_contrasena(longitud)


if __name__ == "__main__":
    unittest.main()
