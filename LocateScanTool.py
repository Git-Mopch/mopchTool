import os
import subprocess
import platform
import nmap
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from colorama import Fore


class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)


def whoRU(tarjet):
    sistema = platform.system()
    ruta_local_nmap = os.path.join(os.getcwd(), "tools", "nmap.exe")

    if sistema == "Windows":
        ruta_nmap = ruta_local_nmap
        if not os.path.isfile(ruta_nmap):
            print(f"[!] No se encontró 'nmap.exe' en: {ruta_nmap}")
            return []
    elif sistema == "Linux":
        nmap_path = subprocess.run(["which", "nmap"], capture_output=True, text=True)
        ruta_nmap = nmap_path.stdout.strip()
        if not ruta_nmap:
            print("[!] Nmap no está instalado en el sistema. Instálalo con 'sudo apt install nmap'")
            return []
    else:
        print("[!] Este script está diseñado para funcionar en Windows o Linux con Nmap instalado.")
        return []

    subprocess.run("cls" if sistema == "Windows" else "clear", shell=True)
    print(f"[?] Ejecutando escaneo a: {tarjet}")

    loader = Loader("[!] Escaneando puertos...", Fore.LIGHTGREEN_EX + "[+] Escaneo completado!" + Fore.RESET, 0.2).start()

    try:
        resultado = subprocess.run(
            [ruta_nmap, "--unprivileged", "-sT", "-T4", "-p", "1-1000", "-oX", "-", tarjet],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        loader.stop()
        print("[!] Error al ejecutar Nmap:", e.stderr)
        return []

    loader.stop()

    if not resultado.stdout.strip():
        print("[!] Nmap no devolvió salida válida.")
        return []

    nmap_search = [ruta_nmap] if sistema == "Windows" else None
    escaner = nmap.PortScanner(nmap_search_path=nmap_search) if nmap_search else nmap.PortScanner()
    escaner.analyse_nmap_xml_scan(resultado.stdout)

    resultados = []

    for host in escaner.all_hosts():
        print(f"\n [+] Resultados para {Fore.LIGHTRED_EX + host + Fore.RESET}")
        print("Estado del host:", escaner[host].state())

        for protocolo in escaner[host].all_protocols():
            puertos = escaner[host][protocolo].keys()
            for puerto in sorted(puertos):
                info = escaner[host][protocolo].get(puerto)
                if info is None:
                    continue
                resultados.append({
                    "puerto": puerto,
                    "estado": info.get("state", ""),
                    "servicio": info.get("name", ""),
                    "producto": info.get("product", ""),
                    "version": info.get("version", "")
                })
                print(f" - Puerto {puerto}/{protocolo}: {info.get('name', '?')}")