from datetime import datetime
from .paciente import Paciente
from .medico import Medico
from .turno import Turno
from .receta import Receta
from .historia_clinica import HistoriaClinica
from .especialidad import Especialidad
from .excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException, 
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    """
    Clase principal que representa el sistema de gestión de la clínica.
    """
    
    def __init__(self):
        """
        Inicializa una nueva clínica vacía.
        """
        self.__pacientes = {}  # DNI -> Paciente
        self.__medicos = {}    # Matrícula -> Medico
        self.__turnos = []     # Lista de todos los turnos
        self.__historias_clinicas = {}  # DNI -> HistoriaClinica
    
    # === MÉTODOS PARA PACIENTES ===
    
    def agregar_paciente(self, paciente):
        """
        Registra un paciente y crea su historia clínica.
        
        Args:
            paciente (Paciente): El paciente a registrar
            
        Raises:
            ValueError: Si el paciente ya está registrado
        """
        dni = paciente.obtener_dni()
        
        if dni in self.__pacientes:
            raise ValueError(f"El paciente con DNI {dni} ya está registrado")
        
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)
    
    def obtener_pacientes(self):
        """
        Devuelve todos los pacientes registrados.
        
        Returns:
            list[Paciente]: Lista de todos los pacientes
        """
        return list(self.__pacientes.values())
    
    def validar_existencia_paciente(self, dni):
        """
        Verifica si un paciente está registrado.
        
        Args:
            dni (str): DNI del paciente a verificar
            
        Raises:
            PacienteNoEncontradoException: Si el paciente no existe
        """
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"No se encontró paciente con DNI: {dni}")
    
    # === MÉTODOS PARA MÉDICOS ===
    
    def agregar_medico(self, medico):
        """
        Registra un médico.
        
        Args:
            medico (Medico): El médico a registrar
            
        Raises:
            ValueError: Si el médico ya está registrado
        """
        matricula = medico.obtener_matricula()
        
        if matricula in self.__medicos:
            raise ValueError(f"El médico con matrícula {matricula} ya está registrado")
        
        self.__medicos[matricula] = medico
    
    def obtener_medicos(self):
        """
        Devuelve todos los médicos registrados.
        
        Returns:
            list[Medico]: Lista de todos los médicos
        """
        return list(self.__medicos.values())
    
    def obtener_medico_por_matricula(self, matricula):
        """
        Devuelve un médico por su matrícula.
        
        Args:
            matricula (str): Matrícula del médico
            
        Returns:
            Medico: El médico encontrado
            
        Raises:
            ValueError: Si el médico no existe
        """
        if matricula not in self.__medicos:
            raise ValueError(f"No se encontró médico con matrícula: {matricula}")
        
        return self.__medicos[matricula]
    
    def validar_existencia_medico(self, matricula):
        """
        Verifica si un médico está registrado.
        
        Args:
            matricula (str): Matrícula del médico a verificar
            
        Raises:
            ValueError: Si el médico no existe
        """
        if matricula not in self.__medicos:
            raise ValueError(f"No se encontró médico con matrícula: {matricula}")
    
    # === MÉTODOS PARA TURNOS ===
    
    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        """
        Agenda un turno si se cumplen todas las condiciones.
        
        Args:
            dni (str): DNI del paciente
            matricula (str): Matrícula del médico
            especialidad (str): Especialidad solicitada
            fecha_hora (datetime): Fecha y hora del turno
            
        Raises:
            PacienteNoEncontradoException: Si el paciente no existe
            ValueError: Si el médico no existe
            MedicoNoDisponibleException: Si el médico no atiende esa especialidad ese día
            TurnoOcupadoException: Si ya hay un turno para ese médico en esa fecha/hora
        """
        # 1. Validar que el paciente existe
        self.validar_existencia_paciente(dni)
        paciente = self.__pacientes[dni]
        
        # 2. Validar que el médico existe
        self.validar_existencia_medico(matricula)
        medico = self.__medicos[matricula]
        
        # 3. Obtener el día de la semana en español
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        
        # 4. Validar que el médico atiende esa especialidad ese día
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        
        # 5. Validar que no hay turno duplicado
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        
        # 6. Crear y agregar el turno
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        
        # 7. Agregar el turno a la historia clínica del paciente
        self.__historias_clinicas[dni].agregar_turno(turno)
    
    def obtener_turnos(self):
        """
        Devuelve todos los turnos agendados.
        
        Returns:
            list[Turno]: Lista de todos los turnos
        """
        return self.__turnos.copy()
    
    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        """
        Verifica que no haya un turno duplicado.
        
        Args:
            matricula (str): Matrícula del médico
            fecha_hora (datetime): Fecha y hora a verificar
            
        Raises:
            TurnoOcupadoException: Si ya existe un turno para ese médico en esa fecha/hora
        """
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and 
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException(matricula, fecha_hora)
                (f"Ya existe un turno para el médico {matricula} "
                    f"en la fecha {fecha_hora.strftime('%d/%m/%Y %H:%M')}"
                )
    
    # === MÉTODOS PARA RECETAS ===
    
    def emitir_receta(self, dni, matricula, medicamentos):
        """
        Emite una receta para un paciente.
        
        Args:
            dni (str): DNI del paciente
            matricula (str): Matrícula del médico
            medicamentos (list[str]): Lista de medicamentos
            
        Raises:
            PacienteNoEncontradoException: Si el paciente no existe
            ValueError: Si el médico no existe
            RecetaInvalidaException: Si no hay medicamentos
        """
        # 1. Validar que el paciente existe
        self.validar_existencia_paciente(dni)
        paciente = self.__pacientes[dni]
        
        # 2. Validar que el médico existe
        self.validar_existencia_medico(matricula)
        medico = self.__medicos[matricula]
        
        # 3. Validar que hay medicamentos
        if not medicamentos or len(medicamentos) == 0:
            raise RecetaInvalidaException("La receta debe tener al menos un medicamento")
        
        # 4. Validar que no hay medicamentos vacíos
        for medicamento in medicamentos:
            if not medicamento or medicamento.strip() == "":
                raise RecetaInvalidaException("Los medicamentos no pueden estar vacíos")
        
        # 5. Crear y agregar la receta
        receta = Receta(paciente, medico, medicamentos)
        
        # 6. Agregar la receta a la historia clínica del paciente
        self.__historias_clinicas[dni].agregar_receta(receta)
    
    # === MÉTODOS PARA HISTORIA CLÍNICA ===
    
    def obtener_historia_clinica(self, dni):
        """
        Devuelve la historia clínica completa de un paciente.
        
        Args:
            dni (str): DNI del paciente
            
        Returns:
            HistoriaClinica: La historia clínica del paciente
            
        Raises:
            PacienteNoEncontradoException: Si el paciente no existe
        """
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]
    
    # === MÉTODOS AUXILIARES ===
    
    def obtener_dia_semana_en_espanol(self, fecha_hora):
        """
        Traduce un objeto datetime al día de la semana en español.
        
        Args:
            fecha_hora (datetime): Fecha a convertir
            
        Returns:
            str: Día de la semana en español (en minúsculas)
        """
        dias_semana = {
            0: "lunes",
            1: "martes", 
            2: "miércoles",
            3: "jueves",
            4: "viernes",
            5: "sábado",
            6: "domingo"
        }
        return dias_semana[fecha_hora.weekday()]
    
    def obtener_especialidad_disponible(self, medico, dia_semana):
        """
        Obtiene la especialidad disponible para un médico en un día.
        
        Args:
            medico (Medico): El médico
            dia_semana (str): Día de la semana
            
        Returns:
            str: Nombre de la especialidad disponible ese día, o None si no atiende
        """
        return medico.obtener_especialidad_para_dia(dia_semana)
    
    def validar_especialidad_en_dia(self, medico, especialidad_solicitada, dia_semana):
        """
        Verifica que el médico atienda esa especialidad ese día.
        
        Args:
            medico (Medico): El médico
            especialidad_solicitada (str): Especialidad que se solicita
            dia_semana (str): Día de la semana
            
        Raises:
            MedicoNoDisponibleException: Si el médico no atiende esa especialidad ese día
        """
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        
        if especialidad_disponible is None:
            raise MedicoNoDisponibleException(
                f"El médico {medico.obtener_matricula()} no atiende los días {dia_semana}"
            )
        
        if especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException(
                f"El médico {medico.obtener_matricula()} no atiende {especialidad_solicitada} "
                f"los días {dia_semana}. Atiende: {especialidad_disponible}"
            )