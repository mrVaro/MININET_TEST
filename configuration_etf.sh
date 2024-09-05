sudo tc qdisc del dev h2-eth0 root

sudo ethtool -L h2-eth0 tx 4

sudo tc qdisc replace dev h2-eth0 parent root handle 100 taprio \
    num_tc 4 \
    map 2 3 1 0 2 2 2 2 2 2 2 2 2 2 2 2 \
    queues 1@0 1@0 1@0 1@0 \
    base-time 1000000000 \
    sched-entry S 0xC 250000 \
    sched-entry S 0x1 250000 \
    sched-entry S 0x2 250000 \
    sched-entry S 0x4 250000 \
    txtime-delay 300000 \
    flags 0x1 \
    clockid CLOCK_TAI

sudo tc qdisc replace dev h2-eth0 parent 100:1 etf \
    delta 200000 clockid CLOCK_TAI skip_sock_check

