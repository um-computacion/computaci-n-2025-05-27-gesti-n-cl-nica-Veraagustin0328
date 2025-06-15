"""
Excepciones personalizadas para el sistema de gestión de clínica.

Estas excepciones se lanzan cuando ocurren situaciones específicas
del dominio de la clínica médica.
"""


class PacienteNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un paciente por su DNI."""
    def __init__(self, dni):
        self.dni = dni
        super().__init__(f"No se encontró un paciente con DNI: {dni}")


class MedicoNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un médico por su matrícula."""
    def __init__(self, matricula):
        self.matricula = matricula
        super().__init__(f"No se encontró un médico con matrícula: {matricula}")


class MedicoNoDisponibleException(Exception):
    """Excepción lanzada cuando un médico no está disponible para una especialidad o día."""
    def __init__(self, mensaje):
        super().__init__(mensaje)


class TurnoOcupadoException(Exception):
    """Excepción lanzada cuando se intenta agendar un turno en un horario ya ocupado."""
    def __init__(self, matricula, fecha_hora):
        self.matricula = matricula
        self.fecha_hora = fecha_hora
        super().__init__(f"El médico con matrícula {matricula} ya tiene un turno agendado el {fecha_hora}")


class RecetaInvalidaException(Exception):
    """Excepción lanzada cuando se intenta crear una receta inválida."""
    def __init__(self, mensaje):
        super().__init__(mensaje)


class PacienteDuplicadoException(Exception):
    """Excepción lanzada cuando se intenta registrar un paciente que ya existe."""
    def __init__(self, dni):
        self.dni = dni
        super().__init__(f"Ya existe un paciente registrado con DNI: {dni}")


class MedicoDuplicadoException(Exception):
    """Excepción lanzada cuando se intenta registrar un médico que ya existe."""
    def __init__(self, matricula):
        self.matricula = matricula
        super().__init__(f"Ya existe un médico registrado con matrícula: {matricula}")


class EspecialidadDuplicadaException(Exception):
    """Excepción lanzada cuando se intenta agregar una especialidad que ya existe para un médico."""
    def __init__(self, especialidad, matricula):
        self.especialidad = especialidad
        self.matricula = matricula
        super().__init__(f"El médico con matrícula {matricula} ya tiene la especialidad: {especialidad}")


class DatosInvalidosException(Exception):
    """Excepción lanzada cuando se proporcionan datos inválidos."""
    def __init__(self, mensaje):
        super().__init__(mensaje)