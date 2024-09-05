import threading
import os

# Fonction pour exécuter tcpreplay
def replay_pcap(pcap_file):
    os.system(f"tcpreplay --intf1=h2-eth0 --loop=1 {pcap_file}")

# Fichiers PCAP
pcap_files = [
    "pcaps/high_priority.pcap",
    "pcaps/medium_priority.pcap",
    "pcaps/low_priority.pcap"
]

# Créer et démarrer un thread pour chaque fichier PCAP
threads = []
for pcap_file in pcap_files:
    thread = threading.Thread(target=replay_pcap, args=(pcap_file,))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads se terminent
for thread in threads:
    thread.join()

