import os
import subprocess
from colorama import Fore
import time
import sys
import LocateScanTool
import nmap

systemInfo = sys.platform

def print_banner():
    print(Fore.LIGHTWHITE_EX + rf"""
    __  ___                 __  ______            __
   /  |/  /___  ____  _____/ /_/_  __/___  ____  / /
  / /|_/ / __ \/ __ \/ ___/ __ \/ / / __ \/ __ \/ / 
 / /  / / /_/ / /_/ / /__/ / / / / / /_/ / /_/ / /  
/_/  /_/\____/ .___/\___/_/ /_/_/  \____/\____/_/   
            /_/            Hola soy un {Fore.LIGHTMAGENTA_EX + systemInfo + Fore.RESET}                                                                            
      """ + Fore.RESET)

NOMBRE = "mopch"
PASSWD = "032003"

def main_menu():
    red = Fore.LIGHTRED_EX
    purple = Fore.LIGHTMAGENTA_EX
    reset = Fore.RESET

    print(f"""
 [{red}({purple}1{red}){reset}] Escanear Objetivo [Ip o Dominio]
 [{red}({purple}2{red}){reset}] Esconder Archivo
 [{red}({purple}3{red}){reset}] Ejecutar Script
 [{red}({purple}4{red}){reset}] Reconocimiento
 [{red}({purple}5{red}){reset}] Historial redes wifi [Solo Windows]
 [{red}({purple}6{red}){reset}] Documentacion
 [{red}({purple}0{red}){reset}] Salir
          """)
    resp_menu = input("[" + Fore.LIGHTMAGENTA_EX + "?" + Fore.RESET + "] #User > ")
    if resp_menu == "1":
        print("[+] Introduce la IP o Dominio del objetivo:")
        resp_menu = input("[" + Fore.LIGHTMAGENTA_EX + "?" + Fore.RESET + "] #User > ")
        LocateScanTool.whoRU(resp_menu)
    # Agrega más opciones según sea necesario

def check_user(nombre_inp, contrasenya_inp):
    time.sleep(1)
    subprocess.run("cls", shell=True)
    if nombre_inp == NOMBRE and contrasenya_inp == PASSWD:
        print(Fore.LIGHTYELLOW_EX + "[Hola Amigo, ¡Bienvenido!]" + Fore.RESET)
        time.sleep(0.3)
        print("\n[?] ¿Que quieres hacer?")
        time.sleep(0.5)
        main_menu()
    else:
        print(Fore.LIGHTRED_EX + "[X] Usuario o Contraseña incorrecto" + Fore.RESET)

def main():
    print_banner()
   
    try:
        nombre_inp = input(Fore.LIGHTBLACK_EX + "[+] Usuario:" + Fore.WHITE)
        contrasenya_inp = input(Fore.LIGHTBLACK_EX + "[+] Pass:" + Fore.WHITE)
        check_user(nombre_inp, contrasenya_inp)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
        
        
if __name__ == "__main__":
    main()