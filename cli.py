from datetime import datetime
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class CLI:
    """
    Interfaz de línea de comandos para el sistema de gestión de clínica.
    """
    
    def __init__(self):
        """
        Inicializa la CLI con una nueva instancia de clínica.
        """
        self.clinica = Clinica()
    
    def mostrar_menu(self):
        """
        Muestra el menú principal de opciones.
        """
        print("\n" + "="*50)
        print(" SISTEMA DE GESTIÓN DE CLÍNICA")
        print("="*50)
        print("  Agregar paciente")
        print("  Agregar médico")
        print("  Agregar especialidad a médico")
        print("  Agendar turno")
        print("  Emitir receta")
        print("  Ver historia clínica")
        print(" Ver todos los turnos")
        print(" Ver todos los pacientes")
        print(" Ver todos los médicos")
        print(" Salir")
        print("="*50)
    
    def ejecutar(self):
        """
        Ejecuta el bucle principal de la interfaz.
        """
        print("Bienvenido al Sistema de Gestión de Clínica!")
        
        while True:
            try:
                self.mostrar_menu()
                opcion = input(" Seleccione una opción: ").strip()
                
                if opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agregar_especialidad_a_medico()
                elif opcion == "4":
                    self.agendar_turno()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_todos_los_turnos()
                elif opcion == "8":
                    self.ver_todos_los_pacientes()
                elif opcion == "9":
                    self.ver_todos_los_medicos()
                elif opcion == "0":
                    print(" ¡Gracias por usar el sistema! ¡Hasta luego!")
                    break
                else:
                    print(" Opción no válida. Por favor, seleccione una opción del 0 al 9.")
                
                input("\n Presione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n ¡Hasta luego!")
                break
            except Exception as e:
                print(f" Error inesperado: {e}")
                input("\n  Presione Enter para continuar...")
    
    def agregar_paciente(self):
        """
        Solicita datos y agrega un nuevo paciente.
        """
        print("AGREGAR NUEVO PACIENTE")
        print("-" * 30)
        
        try:
            nombre = input(" Nombre completo: ").strip()
            if not nombre:
                print(" El nombre no puede estar vacío.")
                return
            
            dni = input("DNI: ").strip()
            if not dni:
                print(" El DNI no puede estar vacío.")
                return
            
            fecha_nacimiento = input(" Fecha de nacimiento (dd/mm/aaaa): ").strip()
            if not fecha_nacimiento:
                print(" La fecha de nacimiento no puede estar vacía.")
                return
            
            # Validar formato de fecha básicamente
            try:
                datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            except ValueError:
                print(" Formato de fecha inválido. Use dd/mm/aaaa")
                return
            
            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.clinica.agregar_paciente(paciente)
            
            print(f"Paciente {nombre} agregado exitosamente!")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def agregar_medico(self):
        """
        Solicita datos y agrega un nuevo médico.
        """
        print(" AGREGAR NUEVO MÉDICO")
        print("-" * 30)
        
        try:
            nombre = input(" Nombre completo: ").strip()
            if not nombre:
                print(" El nombre no puede estar vacío.")
                return
            
            matricula = input("Matrícula: ").strip()
            if not matricula:
                print(" La matrícula no puede estar vacía.")
                return
            
            medico = Medico(nombre, matricula)
            
            # Solicitar especialidades
            print(" Ahora agregue las especialidades del médico:")
            self.agregar_especialidades_al_crear_medico(medico)
            
            self.clinica.agregar_medico(medico)
            print(f" Médico {nombre} agregado exitosamente!")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def agregar_especialidades_al_crear_medico(self, medico):
        """
        Agrega especialidades a un médico durante su creación.
        """
        while True:
            especialidad_nombre = input("🩺 Nombre de la especialidad (o 'fin' para terminar): ").strip()
            
            if especialidad_nombre.lower() == 'fin':
                break
            
            if not especialidad_nombre:
                print(" El nombre de la especialidad no puede estar vacío.")
                continue
            
            print("Días de atención (separados por comas):")
            print("   Ejemplo: lunes, miércoles, viernes")
            dias_input = input("Días: ").strip()
            
            if not dias_input:
                print("Debe especificar al menos un día.")
                continue
            
            # Procesar días
            dias = [dia.strip().lower() for dia in dias_input.split(",")]
            dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            
            # Validar que todos los días sean válidos
            dias_invalidos = [dia for dia in dias if dia not in dias_validos]
            if dias_invalidos:
                print(f"Días inválidos: {', '.join(dias_invalidos)}")
                print(f"   Días válidos: {', '.join(dias_validos)}")
                continue
            
            try:
                especialidad = Especialidad(especialidad_nombre, dias)
                medico.agregar_especialidad(especialidad)
                print(f"Especialidad {especialidad_nombre} agregada!")
            except Exception as e:
                print(f" Error al agregar especialidad: {e}")
    
    def agregar_especialidad_a_medico(self):
        """
        Agrega una nueva especialidad a un médico existente.
        """
        print("AGREGAR ESPECIALIDAD A MÉDICO")
        print("-" * 40)
        
        try:
            matricula = input("Matrícula del médico: ").strip()
            if not matricula:
                print("La matrícula no puede estar vacía.")
                return
            
            # Verificar que el médico existe
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            
            print(f"Médico encontrado: {medico}")
            
            especialidad_nombre = input("Nombre de la nueva especialidad: ").strip()
            if not especialidad_nombre:
                print("El nombre de la especialidad no puede estar vacío.")
                return
            
            print("Días de atención (separados por comas):")
            dias_input = input("👉 Días: ").strip()
            
            if not dias_input:
                print("Debe especificar al menos un día.")
                return
            
            dias = [dia.strip().lower() for dia in dias_input.split(",")]
            dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            
            dias_invalidos = [dia for dia in dias if dia not in dias_validos]
            if dias_invalidos:
                print(f"Días inválidos: {', '.join(dias_invalidos)}")
                return
            
            especialidad = Especialidad(especialidad_nombre, dias)
            medico.agregar_especialidad(especialidad)
            
            print(f"Especialidad {especialidad_nombre} agregada al médico {medico.obtener_matricula()}!")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def agendar_turno(self):
        """
        Agenda un nuevo turno.
        """
        print("AGENDAR TURNO")
        print("-" * 20)
        
        try:
            dni = input("DNI del paciente: ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                return
            
            matricula = input("Matrícula del médico: ").strip()
            if not matricula:
                print("La matrícula no puede estar vacía.")
                return
            
            especialidad = input("Especialidad: ").strip()
            if not especialidad:
                print("La especialidad no puede estar vacía.")
                return
            
            print("Ingrese fecha y hora del turno:")
            fecha_str = input("   Fecha (dd/mm/aaaa): ").strip()
            hora_str = input("   Hora (HH:MM): ").strip()
            
            if not fecha_str or not hora_str:
                print("La fecha y hora no pueden estar vacías.")
                return
            
            # Parsear fecha y hora
            try:
                fecha_hora_str = f"{fecha_str} {hora_str}"
                fecha_hora = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
            except ValueError:
                print("Formato de fecha/hora inválido. Use dd/mm/aaaa y HH:MM")
                return
            
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado exitosamente!")
            
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, 
                TurnoOcupadoException) as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def emitir_receta(self):
        """
        Emite una nueva receta.
        """
        print("EMITIR RECETA")
        print("-" * 20)
        
        try:
            dni = input("DNI del paciente: ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                return
            
            matricula = input("Matrícula del médico: ").strip()
            if not matricula:
                print("La matrícula no puede estar vacía.")
                return
            
            print("Ingrese los medicamentos (uno por línea, escriba 'fin' para terminar):")
            medicamentos = []
            while True:
                medicamento = input("   Medicamento: ").strip()
                if medicamento.lower() == 'fin':
                    break
                if medicamento:
                    medicamentos.append(medicamento)
                else:
                    print("El medicamento no puede estar vacío.")
            
            if not medicamentos:
                print("Debe agregar al menos un medicamento.")
                return
            
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida exitosamente!")
            
        except (PacienteNoEncontradoException, RecetaInvalidaException) as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def ver_historia_clinica(self):
        """
        Muestra la historia clínica de un paciente.
        """
        print("VER HISTORIA CLÍNICA")
        print("-" * 30)
        
        try:
            dni = input("DNI del paciente: ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                return
            
            historia = self.clinica.obtener_historia_clinica(dni)
            print("\n" + str(historia))
            
        except PacienteNoEncontradoException as e:
            print(f"{e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def ver_todos_los_turnos(self):
        """
        Muestra todos los turnos agendados.
        """
        print("TODOS LOS TURNOS")
        print("-" * 25)
        
        turnos = self.clinica.obtener_turnos()
        
        if not turnos:
            print("No hay turnos agendados.")
            return
        
        for i, turno in enumerate(turnos, 1):
            print(f"{i}. {turno}")
    
    def ver_todos_los_pacientes(self):
        """
        Muestra todos los pacientes registrados.
        """
        print("TODOS LOS PACIENTES")
        print("-" * 30)
        
        pacientes = self.clinica.obtener_pacientes()
        
        if not pacientes:
            print("No hay pacientes registrados.")
            return
        
        for i, paciente in enumerate(pacientes, 1):
            print(f"{i}. {paciente}")
    
    def ver_todos_los_medicos(self):
        """
        Muestra todos los médicos registrados.
        """
        print("TODOS LOS MÉDICOS")
        print("-" * 25)
        
        medicos = self.clinica.obtener_medicos()
        
        if not medicos:
            print("No hay médicos registrados.")
            return
        
        for i, medico in enumerate(medicos, 1):
            print(f"{i}. {medico}")