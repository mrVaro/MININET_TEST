import threading
import os

# Fonction pour exécuter iperf3 client
def run_iperf3(port):
    os.system(f"iperf3 -c 10.0.0.1 -u -b 100K -p {port} -t 240")

# Ports à utiliser
ports = [11000, 21000, 31000]

# Créer et démarrer un thread pour chaque commande iperf3
threads = []
for port in ports:
    thread = threading.Thread(target=run_iperf3, args=(port,))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads se terminent
for thread in threads:
    thread.join()

