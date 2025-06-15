class HistoriaClinica:
    """
    Clase que almacena la información médica de un paciente: turnos y recetas.
    """
    
    def __init__(self, paciente):
        """
        Inicializa una nueva historia clínica para un paciente.
        
        Args:
            paciente (Paciente): El paciente al que pertenece esta historia clínica
        """
        self.__paciente = paciente
        self.__turnos = []  # Lista vacía de turnos
        self.__recetas = []  # Lista vacía de recetas
    
    def agregar_turno(self, turno):
        """
        Agrega un nuevo turno a la historia clínica.
        
        Args:
            turno (Turno): El turno a agregar
        """
        self.__turnos.append(turno)
    
    def agregar_receta(self, receta):
        """
        Agrega una receta médica a la historia clínica.
        
        Args:
            receta (Receta): La receta a agregar
        """
        self.__recetas.append(receta)
    
    def obtener_turnos(self):
        """
        Devuelve una copia de la lista de turnos del paciente.
        
        Returns:
            list[Turno]: Copia de la lista de turnos
        """
        return self.__turnos.copy()
    
    def obtener_recetas(self):
        """
        Devuelve una copia de la lista de recetas del paciente.
        
        Returns:
            list[Receta]: Copia de la lista de recetas
        """
        return self.__recetas.copy()
    
    def __str__(self):
        """
        Devuelve una representación textual de la historia clínica.
        
        Returns:
            str: Representación de la historia clínica con turnos y recetas
        """
        resultado = f"=== Historia Clínica - Paciente: {self.__paciente} ===\n"
        
        # Mostrar turnos
        resultado += f"\n--- TURNOS ({len(self.__turnos)}) ---\n"
        if self.__turnos:
            for i, turno in enumerate(self.__turnos, 1):
                resultado += f"{i}. {turno}\n"
        else:
            resultado += "No hay turnos registrados.\n"
        
        # Mostrar recetas
        resultado += f"\n--- RECETAS ({len(self.__recetas)}) ---\n"
        if self.__recetas:
            for i, receta in enumerate(self.__recetas, 1):
                resultado += f"{i}. {receta}\n"
        else:
            resultado += "No hay recetas registradas.\n"
        
        return resultado