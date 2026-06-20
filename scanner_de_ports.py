import socket
import ipaddress
import time
import threading

cible = input("Entrez l'IP ou un nom de domaine : ")

try:
    #cas où le user entre une IP
    ipaddress.ip_address(cible)
    ip_cible = cible

except ValueError:
    #cas où le user entre un nom de domaine
    try:
        ip_cible = socket.gethostbyname(cible)
        print(f"{cible} correspond à l'IP {ip_cible}")

    except:
        print("Adresse IP ou nom de domaine invalide")
        exit()


try:
    debut_port = int(input("Port de début : "))
    fin_port = int(input("Port de fin : "))

    if debut_port < 0 or fin_port > 65535:
        print("Les ports doivent être compris entre 0 et 65535.")
        exit()

    elif debut_port > fin_port:
        print("Le port de début doit être inférieur au port de fin.")
        exit()

except ValueError:
    print("Veuillez entrer des nombres valides.")
    exit()

ports_ouverts = []
threads = []

debut = time.time()


def scanner_port(ip_cible, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.05)

    resultat = s.connect_ex((ip_cible, port))

    if resultat == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "inconnu"

        ports_ouverts.append((port, service))
        print(f"Port {port} : OUVERT ({service})")

    s.close()


# création et lancement des threads
for port in range(debut_port, fin_port + 1):

    t = threading.Thread(target=scanner_port, args=(ip_cible, port))

    threads.append(t)
    t.start()


#fin de tous les threads
for t in threads:
    t.join()


fin = time.time()

with open("rapport_scan.txt", "w") as fichier:

    fichier.write("=== Rapport du scan ===\n")
    fichier.write(f"Cible : {cible}\n\n")

    fichier.write("Ports ouverts :\n")

    for port, service in sorted(ports_ouverts):
        fichier.write(f"Port {port} : {service}\n")

    fichier.write(f"\nNombre de ports ouverts : {len(ports_ouverts)}\n")
    fichier.write(
        f"Temps du scan : {round(fin - debut, 2)} secondes\n"
    )

print("\nLe rapport du scan se trouve dans le fichier rapport_scan.txt")
