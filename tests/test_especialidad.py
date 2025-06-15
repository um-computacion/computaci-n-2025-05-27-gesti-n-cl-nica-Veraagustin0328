import unittest
from modelo.especialidad import Especialidad
from modelo.excepciones import DatosInvalidosException

class TestEspecialidad(unittest.TestCase):
    def test_creacion_especialidad_valida(self):
        esp = Especialidad("Dermatología", ["lunes", "viernes"])
        self.assertIn("lunes", esp.obtener_dias())

    def test_dia_invalido(self):
        with self.assertRaises(DatosInvalidosException):
            Especialidad("Oftalmología", ["funday"])

    def test_dia_vacio(self):
        with self.assertRaises(DatosInvalidosException):
            Especialidad("Neurología", [""])

    def test_tipo_vacio(self):
        with self.assertRaises(DatosInvalidosException):
            Especialidad("", ["lunes"])
