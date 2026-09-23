import unittest
from tkinter import ttk
from unittest.mock import patch

from generador import crear_ventana


def buscar_controles(raiz):
    for hijo in raiz.winfo_children():
        yield hijo
        yield from buscar_controles(hijo)


class TestInterfaz(unittest.TestCase):
    def test_generar_y_copiar(self):
        ventana = crear_ventana()
        try:
            ventana.update()
            controles = list(buscar_controles(ventana))
            entrada = next(c for c in controles if c.winfo_name() == "longitud")
            salida = next(c for c in controles if c.winfo_name() == "resultado")
            self.assertIs(type(salida), ttk.Label)

            def texto_resultado():
                return ventana.getvar(salida.cget("textvariable"))

            generar = next(
                c for c in controles
                if isinstance(c, ttk.Button) and c.cget("text") == "Generar contraseña"
            )
            copiar = next(
                c for c in controles
                if isinstance(c, ttk.Button) and c.cget("text") == "Copiar"
            )

            self.assertIs(type(entrada), ttk.Entry)
            self.assertTrue(copiar.instate(["disabled"]))
            self.assertEqual(entrada.get(), "20")
            generar.invoke()
            ventana.update_idletasks()
            self.assertEqual(len(texto_resultado()), 20)
            altura_corta = salida.winfo_height()

            entrada.delete(0, "end")
            entrada.insert(0, "12")
            entrada.focus_force()
            entrada.event_generate("<Return>")
            ventana.update()
            self.assertEqual(len(texto_resultado()), 12)

            entrada.delete(0, "end")
            entrada.insert(0, "128")
            generar.invoke()
            ventana.update_idletasks()
            self.assertEqual(len(texto_resultado()), 128)
            self.assertGreater(salida.winfo_height(), altura_corta)
            self.assertFalse(copiar.instate(["disabled"]))

            with patch.object(ventana, "clipboard_clear"):
                with patch.object(ventana, "clipboard_append") as guardar:
                    copiar.invoke()
                    guardar.assert_called_once_with(texto_resultado())

            entrada.delete(0, "end")
            entrada.insert(0, "8")
            generar.invoke()
            self.assertEqual(texto_resultado(), "")
            self.assertTrue(copiar.instate(["disabled"]))
        finally:
            ventana.destroy()


if __name__ == "__main__":
    unittest.main()
