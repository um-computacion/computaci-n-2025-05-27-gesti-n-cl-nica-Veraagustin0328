import unittest
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico
from datetime import datetime

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Mario Ruiz", "11223344", "10/10/1985")
        self.medico = Medico("Dra. Suárez", "S777")
        self.medicamentos = ["Paracetamol", "Amoxicilina"]

    def test_receta_valida(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("S777", str(receta))
