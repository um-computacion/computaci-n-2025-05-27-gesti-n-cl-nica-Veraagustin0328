#!/usr/bin/env python3
"""
Sistema de Gestión para una Clínica

Este es el punto de entrada principal para el sistema de gestión de clínica.
Ejecute este archivo para iniciar la interfaz de línea de comandos.

Autor: Agustin Vera
Fecha: 12/06/2025
Materia: Computacion I
"""

from cli import CLI

def main():
    """
    Función principal que inicia el sistema de gestión de clínica.
    """
    try:
        # Crear e iniciar la interfaz de línea de comandos
        cli = CLI()
        cli.ejecutar()
        
    except KeyboardInterrupt:
        print(" Sistema interrumpido por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f" Error crítico del sistema: {e}")
        print("Por favor, contacte al administrador del sistema.")

if __name__ == "__main__":
    main()