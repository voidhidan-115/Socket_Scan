import socket

# --- PHASE DE CONFIGURATION ---

# Creation de la variable addresse ip 
ip_cible = input("Entrez l'ip cible : ") 

if "." not in ip_cible:
    print("Veuillez rentrez une ip valide")
    exit()

# Creation de la liste des ports à scanner 
ports_cible = []

# Creation de la boucle d'ajout 
while True: 
    port = input("Port (Entrée pour lancer le scan) : ")

    # Break de la boucle si entier vide
    if port == "":
        break 
        
    # Si la saisie est bien un nombre strg conversion en int avant d'ajouter a la liste
    if port.isdigit():
        ports_cible.append(int(port))
    else :
        print("Ce n'est pas un nombre")

# Fin de la boucle, vérification de la liste des ports
print(f"Fin de saisie. {len(ports_cible)} ports enregistrés dans la file d'attente.")


# --- DÉFINITION DES OUTILS ---

# Creation fonction Scan
def scan_port(ip_cible, port_cible):
    ports_ouvert = [] # Liste locale pour stocker les succès

    # On boucle et tente chaque port
    for port in port_cible:
        try: 
             # AF_INET gere l'ipv4 et SOCK_STREAM le TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            résultat_scan = s.connect_ex((ip_cible, port))
            
            # Si la valeur passe a 0 le port est ouvert
            if résultat_scan == 0:
                print(f"Port {port} : OUVERT")
                ports_ouvert.append(port)

            s.close()

        except Exception as erreur:
            # On affiche l'erreur et la boucle for passe au port suivant
            print(f"Saut du port {port} à cause d'une erreur : {erreur}")
            
    return ports_ouvert # Retourne la liste une fois la boucle terminée

def export_ports(liste_ports, file_name="scan_results.txt"):
    try:
        # Utilisation de 'w' pour créer/écraser le fichier
        with open(file_name, "w") as export :
            # On écrit un en-tête pour le rapport
            export.write(f"--- RESULTATS DU SCAN SUR {ip_cible} ---\n")
            
            # On boucle sur la liste pour écrire chaque port un par un
            for port in liste_ports:
                export.write(f"Port ouvert : {port}\n")
                
        print(f" Succès : {len(liste_ports)} ports exportés dans {file_name}")
    except Exception as e:
        print(f" Erreur lors de l'écriture du fichier : {e}")


# --- POINT D'ENTRÉE DU SCRIPT (MAIN) ---

if __name__ == "__main__":
    print("  AUDIT DE RECONNAISSANCE TCP  ")
  
    #  On lance le scan et on récupère les ports ouverts
    resultats = scan_port(ip_cible, ports_cible)
    
    # On exporte les résultats si on en a trouvé
    if resultats:
        export_ports(resultats)
    else:
        print(" Aucun port ouvert détecté. Aucun rapport généré.")
        
    print("\nMission terminée.")