"""
Clase Paciente.

Contiene al paciente con sus datos basicos, nombre, fecha de nacimiento, DNI.
"""

from .excepciones import DatosInvalidosException


class Paciente:
    """
    Representa a un paciente de la clínica.
    
    Atributos:
        __nombre (str): Nombre completo del paciente
        __dni (str): DNI del paciente (identificador único)
        __fecha_nacimiento (str): Fecha de nacimiento en formato dd/mm/aaaa
    """
    
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        """
        Inicializa un nuevo paciente.
        
        Args:
            nombre (str): Nombre completo del paciente
            dni (str): DNI del paciente
            fecha_nacimiento (str): Fecha de nacimiento en formato dd/mm/aaaa
            
        Raises:
            DatosInvalidosException: Si algún parámetro está vacío o es None
        """
        # Validaciones
        if not nombre or not nombre.strip():
            raise DatosInvalidosException("El nombre del paciente no puede estar vacío")
        
        if not dni or not dni.strip():
            raise DatosInvalidosException("El DNI del paciente no puede estar vacío")
            
        if not fecha_nacimiento or not fecha_nacimiento.strip():
            raise DatosInvalidosException("La fecha de nacimiento no puede estar vacía")
        
        # Validar formato básico de fecha (dd/mm/aaaa)
        if not self._validar_formato_fecha(fecha_nacimiento.strip()):
            raise DatosInvalidosException("La fecha debe tener formato dd/mm/aaaa")
        
        # Asignar atributos privados
        self.__nombre = nombre.strip()
        self.__dni = dni.strip()
        self.__fecha_nacimiento = fecha_nacimiento.strip()
    
    def _validar_formato_fecha(self, fecha: str) -> bool:
        """
        Valida que la fecha tenga el formato básico dd/mm/aaaa.
        
        Args:
            fecha (str): Fecha a validar
            
        Returns:
            bool: True si el formato es correcto, False en caso contrario
        """
        try:
            partes = fecha.split('/')
            if len(partes) != 3:
                return False
            
            dia, mes, anio = partes
            
            # Verificar que sean números y tengan la longitud correcta
            if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
                return False
                
            if len(dia) != 2 or len(mes) != 2 or len(anio) != 4:
                return False
            
            # Verificar rangos básicos
            dia_int = int(dia)
            mes_int = int(mes)
            anio_int = int(anio)
            
            if not (1 <= dia_int <= 31):
                return False
            if not (1 <= mes_int <= 12):
                return False
            if not (1900 <= anio_int <= 2024):
                return False
                
            return True
            
        except (ValueError, AttributeError):
            return False
    
    def obtener_dni(self) -> str:
        """
        Devuelve el DNI del paciente.
        
        Returns:
            str: DNI del paciente
        """
        return self.__dni
    
    def obtener_nombre(self) -> str:
        """
        Devuelve el nombre del paciente.
        
        Returns:
            str: Nombre completo del paciente
        """
        return self.__nombre
    
    def obtener_fecha_nacimiento(self) -> str:
        """
        Devuelve la fecha de nacimiento del paciente.
        
        Returns:
            str: Fecha de nacimiento en formato dd/mm/aaaa
        """
        return self.__fecha_nacimiento
    
    def __str__(self) -> str:
        """
        Representación en texto del paciente.
        
        Returns:
            str: Información legible del paciente
        """
        return f"Paciente: {self.__nombre} (DNI: {self.__dni}) - Nacido el {self.__fecha_nacimiento}"
    
    def __eq__(self, other) -> bool:
        """
        Compara dos pacientes por su DNI.
        
        Args:
            other: Otro paciente a comparar
            
        Returns:
            bool: True si tienen el mismo DNI, False en caso contrario
        """
        if isinstance(other, Paciente):
            return self.__dni == other.__dni
        return False
    
    def __hash__(self) -> int:
        """
        Genera hash basado en el DNI para usar en sets y diccionarios.
        
        Returns:
            int: Hash del DNI
        """
        return hash(self.__dni)
