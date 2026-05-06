import socket 

#Creation de la variable addresse ip 
ip_cible = input("Entrez l'ip cible") 

if "." not in ip_cible:
    print("Veuillez rentrez une ip valide")
    exit()

#Creation de la liste des ports à scanner 
ports_cible = []

#Creation de la boucle d'ajout 
 while True: 
    port = input("Port : ")

#Break de la boucle si entier vide
    if port == "":
        break 
#Si la saisie est bien un nombre strg conversion en int avant d'ajouter a la liste
    if port.isdigit():
        ports_cible.append(int(port))
    
    else :
        print("Ce n'est pas un nombre")

#Fin de la boucle, vérification de la liste des ports
print(f"Fin de saisie. {len(ports_cible)} ports enregistrés dans la file d'attente.")


ports_ouvert = []

#Creation fonction Scan
def scan_port(ip_cible, port_cible):

    #On boucle et tente chaque port
    for port in port_cible:
        try: 
             
             #AF_INET gere l'ipv4 et SOCK_STREAM le TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            résultat_scan = s.connect_ex((ip_cible, port))
            
            #Si la valeur passe a 0 le port est ouvert
            if résultat_scan == 0:
                print(f"Port {port} : OUVERT")
                ports_ouvert.append(port)

            s.close()

        except Exception as erreur:
            # On affiche l'erreur et la boucle for passe au port suivant
            print(f"Saut du port {port} à cause d'une erreur : {erreur}")
return ports_ouvert

def export_ports(ports_ouvert, file_name="/tmp/scan_results.txt"):
    try:
        with open(file_name, "w") as file_name :
            # On écrit un en-tête pour le rapport
            export.write("--- RESULTATS DU SCAN ---\n")
            
            # On boucle sur la liste pour écrire chaque port un par un
            for port in ports_ouvert:
                export.write(f"Port ouvert : {port}\n")
                
        print(f" Succès : {len(ports_ouvert)} ports exportés dans {file_name}")
    except Exception as e:
        print(f" Erreur lors de l'écriture du fichier : {e}")