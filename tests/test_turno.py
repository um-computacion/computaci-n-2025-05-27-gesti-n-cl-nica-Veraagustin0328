import unittest
from datetime import datetime, timedelta
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.excepciones import DatosInvalidosException

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Ana Torres", "99887766", "15/05/1990")
        self.medico = Medico("Dr. Luna", "L001")

    def test_crear_turno_valido(self):
        fecha = datetime.now() + timedelta(days=1)
        turno = Turno(self.paciente, self.medico, fecha, "Pediatría")
        self.assertEqual(turno.obtener_paciente(), self.paciente)
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_especialidad(), "Pediatría")

    def test_turno_en_el_pasado(self):
        fecha_pasada = datetime.now() - timedelta(days=1)
        with self.assertRaises(DatosInvalidosException):
            Turno(self.paciente, self.medico, fecha_pasada, "Pediatría")

                  
