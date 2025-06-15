"""
Clase Turno para el sistema de gestión de clínica.

Representa un turno médico entre un paciente y un médico.
"""

from datetime import datetime
from .excepciones import DatosInvalidosException
from .paciente import Paciente
from .medico import Medico


class Turno:
    """
    Representa un turno médico entre un paciente y un médico para una especialidad específica
    en una fecha y hora determinada.
    
    Atributos:
        __paciente (Paciente): Paciente que asiste al turno
        __medico (Medico): Médico asignado al turno
        __fecha_hora (datetime): Fecha y hora del turno
        __especialidad (str): Especialidad médica del turno
    """
    
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        """
        Inicializa un nuevo turno.
        
        Args:
            paciente (Paciente): Paciente que asiste al turno
            medico (Medico): Médico asignado al turno
            fecha_hora (datetime): Fecha y hora del turno
            especialidad (str): Especialidad médica del turno
            
        Raises:
            DatosInvalidosException: Si algún parámetro es inválido
        """
        # Validaciones
        if not isinstance(paciente, Paciente):
            raise DatosInvalidosException("El paciente debe ser una instancia de la clase Paciente")
        
        if not isinstance(medico, Medico):
            raise DatosInvalidosException("El médico debe ser una instancia de la clase Medico")
        
        if not isinstance(fecha_hora, datetime):
            raise DatosInvalidosException("La fecha y hora debe ser una instancia de datetime")
        
        if not especialidad or not especialidad.strip():
            raise DatosInvalidosException("La especialidad no puede estar vacía")
        
        # Verificar que la fecha no sea en el pasado
        if fecha_hora < datetime.now():
            raise DatosInvalidosException("No se pueden agendar turnos en el pasado")
        
        # Asignar atributos privados
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad.strip()
    
    def obtener_paciente(self) -> Paciente:
        """
        Devuelve el paciente asignado al turno.
        
        Returns:
            Paciente: Paciente del turno
        """
        return self.__paciente
    
    def obtener_medico(self) -> Medico:
        """
        Devuelve el médico asignado al turno.
        
        Returns:
            Medico: Médico del turno
        """
        return self.__medico
    
    def obtener_fecha_hora(self) -> datetime:
        """
        Devuelve la fecha y hora del turno.
        
        Returns:
            datetime: Fecha y hora del turno
        """
        return self.__fecha_hora
    
    def obtener_especialidad(self) -> str:
        """
        Devuelve la especialidad del turno.
        
        Returns:
            str: Especialidad médica del turno
        """
        return self.__especialidad
    
    def __str__(self) -> str:
        """
        Devuelve una representación legible del turno.
        
        Returns:
            str: Información completa del turno
        """
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        
        return (f"Turno: {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()}) "
                f"con Dr./Dra. {self.__medico.obtener_nombre()} (Mat: {self.__medico.obtener_matricula()}) "
                f"- {self.__especialidad} - {fecha_str}")
    
    def __eq__(self, other) -> bool:
        """
        Compara dos turnos por médico y fecha/hora.
        
        Args:
            other: Otro turno a comparar
            
        Returns:
            bool: True si son el mismo médico en la misma fecha/hora, False en caso contrario
        """
        if isinstance(other, Turno):
            return (self.__medico.obtener_matricula() == other.__medico.obtener_matricula() and
                    self.__fecha_hora == other.__fecha_hora)
        return False
    
    def __hash__(self) -> int:
        """
        Genera hash basado en médico y fecha/hora.
        
        Returns:
            int: Hash del turno
        """
        return hash((self.__medico.obtener_matricula(), self.__fecha_hora))