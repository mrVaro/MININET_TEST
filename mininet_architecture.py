from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController

def create_topology():
    # Création de l'instance de Mininet
    net = Mininet(controller=RemoteController)

    # Ajout des hôtes
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    # Ajout du switch
    s1 = net.addSwitch('s1')

    # Liaisons entre les hôtes et le switch
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Démarrage du contrôleur Ryu (par exemple) en arrière-plan
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Démarrage du réseau
    net.start()

    # Affichage de l'interface CLI Mininet pour tester le réseau
    CLI(net)

    # Arrêt du réseau à la fermeture de l'interface CLI
    net.stop()

if __name__ == '__main__':
    # Appel de la fonction pour créer la topologie
    create_topology()


