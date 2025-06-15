import unittest
from modelo.historia_clinica import HistoriaClinica
from modelo.paciente import Paciente
from modelo.receta import Receta
from modelo.turno import Turno
from modelo.medico import Medico
from datetime import datetime, timedelta

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Laura González", "55443322", "20/06/1992")
        self.historia = HistoriaClinica(self.paciente)
        self.medico = Medico("Dr. Bravo", "B001")
        self.turno = Turno(self.paciente, self.medico, datetime.now() + timedelta(days=1), "Clínica")
        self.receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])

    def test_agregar_y_obtener_turno(self):
        self.historia.agregar_turno(self.turno)
        self.assertEqual(len(self.historia.obtener_turnos()), 1)

    def test_agregar_y_obtener_receta(self):
        self.historia.agregar_receta(self.receta)
        self.assertEqual(len(self.historia.obtener_recetas()), 1)
