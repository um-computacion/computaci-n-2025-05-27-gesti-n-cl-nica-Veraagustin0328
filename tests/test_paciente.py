"""
Tests para la clase Paciente.
"""

import unittest
import sys
import os

# Agregar el directorio padre al path para importar modelo
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.paciente import Paciente
from modelo.excepciones import DatosInvalidosException


class TestPaciente(unittest.TestCase):
    """Tests para la clase Paciente."""
    
    def test_crear_paciente_valido(self):
        """Test: Crear un paciente con datos válidos."""
        paciente = Paciente("Juan Pérez", "12345678", "15/08/1990")
        
        self.assertEqual(paciente.obtener_nombre(), "Juan Pérez")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(paciente.obtener_fecha_nacimiento(), "15/08/1990")
    
    def test_crear_paciente_nombre_vacio(self):
        """Test: Error al crear paciente con nombre vacío."""
        with self.assertRaises(DatosInvalidosException) as context:
            Paciente("", "12345678", "15/08/1990")
        
        self.assertIn("nombre", str(context.exception).lower())
    
    def test_crear_paciente_dni_vacio(self):
        """Test: Error al crear paciente con DNI vacío."""
        with self.assertRaises(DatosInvalidosException) as context:
            Paciente("Juan Pérez", "", "15/08/1990")
        
        self.assertIn("dni", str(context.exception).lower())
    
    def test_crear_paciente_fecha_vacia(self):
        """Test: Error al crear paciente con fecha vacía."""
        with self.assertRaises(DatosInvalidosException) as context:
            Paciente("Juan Pérez", "12345678", "")
        
        self.assertIn("fecha", str(context.exception).lower())
    
    def test_crear_paciente_fecha_formato_invalido(self):
        """Test: Error al crear paciente con formato de fecha inválido."""
        with self.assertRaises(DatosInvalidosException) as context:
            Paciente("Juan Pérez", "12345678", "1990-08-15")
        
        self.assertIn("formato", str(context.exception).lower())
    
    def test_crear_paciente_fecha_dia_invalido(self):
        """Test: Error al crear paciente con día inválido."""
        with self.assertRaises(DatosInvalidosException) as context:
            Paciente("Juan Pérez", "12345678", "32/08/1990")
        
        self.assertIn("formato", str(context.exception).lower())
    
    def test_crear_paciente_fecha_mes_invalido(self):
        """Test: Error al crear paciente con mes inválido."""
        with self.assertRaises(DatosInvalidosException) as context:
            Paciente("Juan Pérez", "12345678", "15/13/1990")
        
        self.assertIn("formato", str(context.exception).lower())
    
    def test_crear_paciente_con_espacios(self):
        """Test: Crear paciente con espacios extra (deben eliminarse)."""
        paciente = Paciente("  Juan Pérez  ", "  12345678  ", "  15/08/1990  ")
        
        self.assertEqual(paciente.obtener_nombre(), "Juan Pérez")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(paciente.obtener_fecha_nacimiento(), "15/08/1990")
    
    def test_str_paciente(self):
        """Test: Representación en string del paciente."""
        paciente = Paciente("Juan Pérez", "12345678", "15/08/1990")
        str_paciente = str(paciente)
        
        self.assertIn("Juan Pérez", str_paciente)
        self.assertIn("12345678", str_paciente)
        self.assertIn("15/08/1990", str_paciente)
    
    def test_igualdad_pacientes(self):
        """Test: Dos pacientes con el mismo DNI son iguales."""
        paciente1 = Paciente("Juan Pérez", "12345678", "15/08/1990")
        paciente2 = Paciente("Juan García", "12345678", "20/05/1985")
        
        self.assertEqual(paciente1, paciente2)
    
    def test_desigualdad_pacientes(self):
        """Test: Dos pacientes con diferente DNI son diferentes."""
        paciente1 = Paciente("Juan Pérez", "12345678", "15/08/1990")
        paciente2 = Paciente("Juan García", "87654321", "20/05/1985")
        
        self.assertNotEqual(paciente1, paciente2)


if __name__ == '__main__':
    unittest.main()