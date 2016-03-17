#
sudo scapy

ans,unans=sr( IP(dst="192.168.1.*")/TCP(dport=80,flags="S") )


ans.summary( lambda(s,r) : r.sprintf("%IP.src% is alive") )
