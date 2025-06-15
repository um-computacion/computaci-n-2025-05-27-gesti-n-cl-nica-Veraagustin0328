import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import DatosInvalidosException, EspecialidadDuplicadaException

class TestMedico(unittest.TestCase):
    def test_creacion_medico_valido(self):
        medico = Medico("Dr. House", "ABC123")
        self.assertEqual(medico.obtener_matricula(), "ABC123")

    def test_medico_nombre_vacio(self):
        with self.assertRaises(DatosInvalidosException):
            Medico("", "ABC123")

    def test_agregar_especialidad(self):
        medico = Medico("Dra. Grey", "XYZ789")
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        medico.agregar_especialidad(esp)
        self.assertIn(esp, medico.obtener_especialidades())

    def test_especialidad_duplicada(self):
        medico = Medico("Dra. Wilson", "M123")
        esp1 = Especialidad("Pediatría", ["martes"])
        esp2 = Especialidad("pediatría", ["jueves"])  # mismo tipo
        medico.agregar_especialidad(esp1)
        with self.assertRaises(EspecialidadDuplicadaException):
            medico.agregar_especialidad(esp2)
