from scapy.all import *
import texttable as tt


tab = tt.Texttable()
headings = ['MAC_Addr','IP']
tab.header(headings)

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('/home/kali/Desktop/misc/Project/Bayer/CRU/CRU-service-port.pcapng')

#null list
unique_mac = []
unique_ip = []
ignore_mac = ['70:88:6b:80:98:ec']

# Let's iterate through every packet
for packet in packets:
    if packet.haslayer(IP):
        print(packet.fields['src'] , " - " , packet[IP].src)
        if packet.fields['src'] not in unique_mac:
            if packet.fields['src'] not in ignore_mac:
                unique_mac.append(packet.fields['src'])
                unique_ip.append(packet[IP].src)




for row in zip(unique_mac, unique_ip):
    tab.add_row(row)


s = tab.draw()
print(s)

