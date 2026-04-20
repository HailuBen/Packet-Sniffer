from scapy.all import sniff, Ether, IP, TCP, UDP, conf
from datetime import datetime

# Python dict, great for organization. Everything in one place
FILTER_OPTIONS = {
    "1": ("All IP",      "ip"), # "key": "display label", "filter string for scapy"  
    "2": ("TCP",         "tcp"),
    "3": ("UDP",         "udp"),
    "4": ("HTTP",        "tcp port 80"),
    "5": ("HTTPS",       "tcp port 443"),
    "6": ("DNS",         "udp port 53"),
}

# stylistic choice
def print_banner():
    print("""
╔══════════════════════════════════════════╗
║           Raw Packet Sniffer             ║
║       Running on Windows via Npcap       ║
╚══════════════════════════════════════════╝
    """)

# extract relevant protocol layers, print summary. runs for every captured packet
def process_packet(packet):
    time = datetime.now().strftime("%H:%M:%S")  # timestamp e.x 23:16:30

    # check if packet contains Ethernet or IP layer
    eth = packet[Ether] if Ether in packet else None
    ip  = packet[IP]    if IP    in packet else None
     
    if eth:
        print(f"\n[{time}] {eth.src} → {eth.dst}")  
        # if ethernet, print MAC addresses (source → destination)
    if ip:
        print(f"  IP  {ip.src} → {ip.dst}  TTL={ip.ttl}")
        # if IP layer exists, print IP addresses, Time to live   


    if ip and TCP in packet:    # check for ip and TCP layers
        tcp = packet[TCP]   # extract TCP layer obj from packet
        print(f"  TCP {tcp.sport} → {tcp.dport}  Flags={tcp.flags}")    
        # print tcp sourceport → tcp destinationport, and tcp flags (SYN, ACK, FIN, etc.)
            # e.x. Flags=A → ACKnowledgement. Flags=PA → Push, ACKnowledgement
        
    elif ip and UDP in packet:  # check for ip, UDP
        udp = packet[UDP]   # extract UDP header 
        print(f"  UDP {udp.sport} → {udp.dport}")   # print source, destination. (UDP has no flags)

# MAIN: handles user input, starts sniffer
def main():
    print_banner()
    
    # List all available Npcap Network Interfaces
    ifaces = list(conf.ifaces.values())
    print("Interfaces:")
    for i, iface in enumerate(ifaces):
        print(f"  [{i}] {iface.name}")
    iface = ifaces[int(input("Pick interface: "))].name   # user inputs number here 

    # Protocol Filters
    print("\nFilters:")
    for key, (label, _) in FILTER_OPTIONS.items():
        print(f"  [{key}] {label}")  # e.x. [1] All IP, [2] TCP
    bpf = FILTER_OPTIONS.get(input("Pick filter: "), ("", "ip"))[1]


    running = True
    def stop_capture(packet):
        return not running
        # allows program to halt & send "Stopped." message, 
    # better for maintainability & potential future additions

    try:
        sniff(iface=iface, prn=process_packet, filter=bpf, store=False, stop_filter=stop_capture)
        # sniff le packets, 
            # parameters: interface, callback (print) fuction, Berkley Packet Filter, Do NOT store in memory to avoid leaks, custom stop function
    except KeyboardInterrupt:
        pass
    finally:
        print("\nStopped.") # ensure block prints, even if Ctrl+C is swallowed by Scapy/Windows

if __name__ == "__main__":
    main()