"""
Clase Medico para el sistema de gestión de clínica.

Representa a un médico con su matrícula y especialidades.
"""

from .excepciones import DatosInvalidosException, EspecialidadDuplicadaException
from .especialidad import Especialidad


class Medico:
    """
    Representa a un médico del sistema, con sus especialidades y matrícula profesional.
    
    Atributos:
        __nombre (str): Nombre completo del médico
        __matricula (str): Matrícula profesional del médico (clave única)
        __especialidades (list[Especialidad]): Lista de especialidades con sus días de atención
    """
    
    def __init__(self, nombre: str, matricula: str):
        """
        Inicializa un nuevo médico.
        
        Args:
            nombre (str): Nombre completo del médico
            matricula (str): Matrícula profesional del médico
            
        Raises:
            DatosInvalidosException: Si algún parámetro está vacío o es None
        """
        # Validaciones
        if not nombre or not nombre.strip():
            raise DatosInvalidosException("El nombre del médico no puede estar vacío")
        
        if not matricula or not matricula.strip():
            raise DatosInvalidosException("La matrícula del médico no puede estar vacía")
        
        # Asignar atributos privados
        self.__nombre = nombre.strip()
        self.__matricula = matricula.strip()
        self.__especialidades = []
    
    def agregar_especialidad(self, especialidad: Especialidad):
        """
        Agrega una especialidad a la lista del médico.
        
        Args:
            especialidad (Especialidad): Especialidad a agregar
            
        Raises:
            DatosInvalidosException: Si la especialidad es None
            EspecialidadDuplicadaException: Si la especialidad ya existe
        """
        if not isinstance(especialidad, Especialidad):
            raise DatosInvalidosException("La especialidad debe ser una instancia de la clase Especialidad")
        
        # Verificar si ya existe esta especialidad
        for esp_existente in self.__especialidades:
            if esp_existente.obtener_especialidad().lower() == especialidad.obtener_especialidad().lower():
                raise EspecialidadDuplicadaException(
                    especialidad.obtener_especialidad(), 
                    self.__matricula
                )
        
        self.__especialidades.append(especialidad)
    
    def obtener_matricula(self) -> str:
        """
        Devuelve la matrícula del médico.
        
        Returns:
            str: Matrícula del médico
        """
        return self.__matricula
    
    def obtener_nombre(self) -> str:
        """
        Devuelve el nombre del médico.
        
        Returns:
            str: Nombre completo del médico
        """
        return self.__nombre
    
    def obtener_especialidades(self) -> list[Especialidad]:
        """
        Devuelve una copia de la lista de especialidades.
        
        Returns:
            list[Especialidad]: Lista de especialidades del médico
        """
        return self.__especialidades.copy()
    
    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        """
        Devuelve el nombre de la especialidad disponible en el día especificado,
        o None si no atiende ese día.
        
        Args:
            dia (str): Día de la semana a consultar
            
        Returns:
            str | None: Nombre de la especialidad disponible, o None si no atiende
        """
        if not dia or not dia.strip():
            return None
        
        dia_normalizado = dia.strip().lower()
        
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia_normalizado):
                return especialidad.obtener_especialidad()
        
        return None
    
    def tiene_especialidad(self, nombre_especialidad: str) -> bool:
        """
        Verifica si el médico tiene una especialidad específica.
        
        Args:
            nombre_especialidad (str): Nombre de la especialidad a verificar
            
        Returns:
            bool: True si tiene la especialidad, False en caso contrario
        """
        if not nombre_especialidad or not nombre_especialidad.strip():
            return False
        
        nombre_normalizado = nombre_especialidad.strip().lower()
        
        for especialidad in self.__especialidades:
            if especialidad.obtener_especialidad().lower() == nombre_normalizado:
                return True
        
        return False
    
    def atiende_especialidad_en_dia(self, nombre_especialidad: str, dia: str) -> bool:
        """
        Verifica si el médico atiende una especialidad específica en un día determinado.
        
        Args:
            nombre_especialidad (str): Nombre de la especialidad
            dia (str): Día de la semana
            
        Returns:
            bool: True si atiende esa especialidad ese día, False en caso contrario
        """
        if not nombre_especialidad or not dia:
            return False
        
        nombre_normalizado = nombre_especialidad.strip().lower()
        dia_normalizado = dia.strip().lower()
        
        for especialidad in self.__especialidades:
            if (especialidad.obtener_especialidad().lower() == nombre_normalizado and 
                especialidad.verificar_dia(dia_normalizado)):
                return True
        
        return False
    
    def __str__(self) -> str:
        """
        Representación legible del médico, incluyendo matrícula y especialidades.
        
        Returns:
            str: Información completa del médico
        """
        especialidades_str = []
        for esp in self.__especialidades:
            especialidades_str.append(str(esp))
        
        if especialidades_str:
            esp_texto = "\n  - ".join(especialidades_str)
            return f"Dr./Dra. {self.__nombre} (Matrícula: {self.__matricula})\nEspecialidades:\n  - {esp_texto}"
        else:
            return f"Dr./Dra. {self.__nombre} (Matrícula: {self.__matricula})\nEspecialidades: Ninguna registrada"
    
    def __eq__(self, other) -> bool:
        """
        Compara dos médicos por su matrícula.
        
        Args:
            other: Otro médico a comparar
            
        Returns:
            bool: True si tienen la misma matrícula, False en caso contrario
        """
        if isinstance(other, Medico):
            return self.__matricula == other.__matricula
        return False
    
    def __hash__(self) -> int:
        """
        Genera hash basado en la matrícula para usar en sets y diccionarios.
        
        Returns:
            int: Hash de la matrícula
        """
        return hash(self.__matricula)