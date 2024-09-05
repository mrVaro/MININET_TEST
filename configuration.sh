# Supprimer les qdiscs existants

sudo tc qdisc del dev h2-eth0 root

# Supprimer les règles existantes
sudo iptables -t mangle -F

sudo ethtool -L h2-eth0 rx 4 tx 4

# Ajouter les règles pour classifier les paquets en fonction de leur dport UDP
sudo iptables -t mangle -A POSTROUTING -p udp --dport 11000 -j CLASSIFY --set-class 1:3
sudo iptables -t mangle -A POSTROUTING -p udp --dport 21000 -j CLASSIFY --set-class 1:1
sudo iptables -t mangle -A POSTROUTING -p udp --dport 31000 -j CLASSIFY --set-class 1:2

# Ajouter et configurer le qdisc taprio
sudo tc qdisc add dev h2-eth0 root handle 100 taprio num_tc 3 map 0 1 2 queues 1@0 1@1 1@2 base-time 1000000000 \
    sched-entry S 01 300000 \
    sched-entry S 02 30000 \
    sched-entry S 04 3000 \
    flags 0x1 \
    clockid CLOCK_TAI

# Ajouter des qdiscs pfifo pour chaque classe après TAPRIO
sudo tc qdisc add dev h2-eth0 parent 100:1 pfifo
sudo tc qdisc add dev h2-eth0 parent 100:2 pfifo
sudo tc qdisc add dev h2-eth0 parent 100:3 pfifo
