from datetime import datetime

class Receta:
    """
    Representa una receta médica emitida por un médico a un paciente.
    """
    
    def __init__(self, paciente, medico, medicamentos):
        """
        Inicializa una nueva receta.
        
        Args:
            paciente (Paciente): El paciente que recibe la receta
            medico (Medico): El médico que emite la receta  
            medicamentos (list[str]): Lista de medicamentos recetados
        """
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos.copy()  # Hacemos una copia para evitar modificaciones externas
        self.__fecha = datetime.now()  # Se asigna automáticamente la fecha actual
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la receta.
        
        Returns:
            str: Representación legible de la receta
        """
        medicamentos_str = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        
        return (f"Receta - Paciente: {self.__paciente.obtener_dni()}, "
                f"Médico: {self.__medico.obtener_matricula()}, "
                f"Medicamentos: {medicamentos_str}, "
                f"Fecha: {fecha_str}")