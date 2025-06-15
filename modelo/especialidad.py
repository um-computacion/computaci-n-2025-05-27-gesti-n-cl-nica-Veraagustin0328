"""
Clase Especialidad para el sistema de gestión de clínica.

Representa una especialidad médica con sus días de atención.
"""

from .excepciones import DatosInvalidosException


class Especialidad:
    """
    Representa una especialidad médica junto con los días de atención asociados.
    
    Atributos:
        __tipo (str): Nombre de la especialidad (ej: "Pediatría", "Cardiología")
        __dias (list[str]): Lista de días en los que se atiende esta especialidad, en minúsculas
    """
    
    # Días válidos de la semana
    DIAS_VALIDOS = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    
    def __init__(self, tipo: str, dias: list[str]):
        """
        Inicializa una nueva especialidad.
        
        Args:
            tipo (str): Nombre de la especialidad
            dias (list[str]): Lista de días de atención
            
        Raises:
            DatosInvalidosException: Si los parámetros son inválidos
        """
        # Validaciones
        if not tipo or not tipo.strip():
            raise DatosInvalidosException("El tipo de especialidad no puede estar vacío")
        
        if not dias or len(dias) == 0:
            raise DatosInvalidosException("Debe especificar al menos un día de atención")
        
        # Validar y normalizar días
        dias_normalizados = []
        for dia in dias:
            if not dia or not dia.strip():
                raise DatosInvalidosException("Los días no pueden estar vacíos")
            
            dia_normalizado = dia.strip().lower()
            
            # Verificar que sea un día válido
            if dia_normalizado not in self.DIAS_VALIDOS:
                raise DatosInvalidosException(f"'{dia}' no es un día válido. Debe ser uno de: {', '.join(self.DIAS_VALIDOS)}")
            
            # Evitar días duplicados
            if dia_normalizado not in dias_normalizados:
                dias_normalizados.append(dia_normalizado)
        
        if len(dias_normalizados) == 0:
            raise DatosInvalidosException("Debe especificar al menos un día válido")
        
        # Asignar atributos privados
        self.__tipo = tipo.strip().title()  # Capitalizar primera letra
        self.__dias = sorted(dias_normalizados)  # Ordenar días alfabéticamente
    
    def obtener_especialidad(self) -> str:
        """
        Devuelve el nombre de la especialidad.
        
        Returns:
            str: Nombre de la especialidad
        """
        return self.__tipo
    
    def obtener_dias(self) -> list[str]:
        """
        Devuelve una copia de la lista de días de atención.
        
        Returns:
            list[str]: Lista de días en minúsculas
        """
        return self.__dias.copy()
    
    def verificar_dia(self, dia: str) -> bool:
        """
        Devuelve True si la especialidad está disponible en el día proporcionado.
        La comparación no es sensible a mayúsculas/minúsculas.
        
        Args:
            dia (str): Día a verificar
            
        Returns:
            bool: True si está disponible ese día, False en caso contrario
        """
        if not dia or not dia.strip():
            return False
        
        dia_normalizado = dia.strip().lower()
        return dia_normalizado in self.__dias
    
    def __str__(self) -> str:
        """
        Devuelve una representación legible de la especialidad.
        
        Returns:
            str: Especialidad con sus días de atención
        """
        # Capitalizar primera letra de cada día para mostrar
        dias_mostrar = [dia.capitalize() for dia in self.__dias]
        dias_texto = ', '.join(dias_mostrar)
        
        return f"{self.__tipo} (Días: {dias_texto})"
    
    def __eq__(self, other) -> bool:
        """
        Compara dos especialidades por su tipo.
        
        Args:
            other: Otra especialidad a comparar
            
        Returns:
            bool: True si tienen el mismo tipo, False en caso contrario
        """
        if isinstance(other, Especialidad):
            return self.__tipo.lower() == other.__tipo.lower()
        return False
    
    def __hash__(self) -> int:
        """
        Genera hash basado en el tipo de especialidad.
        
        Returns:
            int: Hash del tipo de especialidad
        """
        return hash(self.__tipo.lower())