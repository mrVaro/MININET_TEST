iperf3 -s -p 11000 &
iperf3 -s -p 21000 &
iperf3 -s -p 31000 &
sudo tcpdump -i h1-eth0 udp -w captured_traffic.pcap -G 2400 -W 1

