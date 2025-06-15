import unittest
from datetime import datetime, timedelta
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import *
from modelo.turno import Turno

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/2000")
        self.medico = Medico("Dr. García", "M111")
        self.especialidad = Especialidad("Clínica", ["lunes", "martes", "miércoles", "jueves", "viernes"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_exitoso(self):
        fecha = self.__proximo_dia_semana("lunes", hora=10)
        self.clinica.agendar_turno("12345678", "M111", "Clínica", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_agendar_turno_en_dia_erroneo(self):
        fecha = self.__proximo_dia_semana("domingo", hora=10)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M111", "Clínica", fecha)

    def test_turno_duplicado(self):
        fecha = self.__proximo_dia_semana("lunes", hora=9)
        self.clinica.agendar_turno("12345678", "M111", "Clínica", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "M111", "Clínica", fecha)

    def test_emitir_receta_exitosa(self):
        medicamentos = ["Ibuprofeno"]
        self.clinica.emitir_receta("12345678", "M111", medicamentos)
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M111", [])

    def __proximo_dia_semana(self, dia_nombre: str, hora: int = 9) -> datetime:
        dias = {
            "lunes": 0, "martes": 1, "miércoles": 2,
            "jueves": 3, "viernes": 4, "sábado": 5, "domingo": 6
        }
        hoy = datetime.now()
        objetivo = dias[dia_nombre]
        dias_adelante = (objetivo - hoy.weekday() + 7) % 7 or 7
        proxima_fecha = hoy + timedelta(days=dias_adelante)
        return proxima_fecha.replace(hour=hora, minute=0, second=0, microsecond=0)
