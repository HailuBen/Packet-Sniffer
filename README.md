# Raw Packet Sniffer & Protocol Analyzer
A command-line packet sniffer built in Python using Scapy. Captures raw Ethernet frames and decodes IP, TCP, UDP, and ICMP headers in real time.
---
 
## Requirements
 
- Python 3.x
- [Npcap](https://npcap.com) — must be installed before running *(Windows only)*
- Scapy
Install Scapy via pip:
 
```
pip install scapy
```
 
> **Note:** Npcap must be installed with "WinPcap API-compatible mode" checked. This is what gives Python access to raw Ethernet frames on Windows.
 
---
## How to Run
 
1. **Open your terminal as Administrator**
   Raw sockets require elevated privileges on Windows. Right-click your terminal or VS Code and select *Run as Administrator*.
2. **Run the script**

   ```
   python sniffer.py
   ```
 
4. **Pick a network interface**
   The script lists all available interfaces. Enter the number that corresponds to your active connection (Wi-Fi or Ethernet).
5. **Pick a capture filter**
   Choose from the menu:
   | Option | Filter |
   |--------|--------|
   | 1 | All IP traffic |
   | 2 | TCP only |
   | 3 | UDP only |
   | 4 | HTTP (port 80) |
   | 5 | HTTPS (port 443) |
   | 6 | DNS (port 53) |
6. **Watch packets appear in the console**
   Each captured packet displays its timestamp, MAC addresses, IP addresses, TTL, protocol, and port numbers.
7. **Stop the capture**
   Press `Ctrl+C` at any time.
---

## What It Displays
 
```
[23:16:50] f0:2f:74:14:cb:38 → 34:db:9c:86:a4:90
  IP  192.168.2.32 → 142.250.139.94  TTL=128
  UDP 58620 → 443
```
 
| Field | Description |
|-------|-------------|
| Timestamp | Time the packet was captured |
| MAC addresses | Source and destination at the Ethernet (Layer 2) level |
| IP addresses | Source and destination at the network (Layer 3) level |
| TTL | Time To Live — how many hops remain before the packet is dropped |
| Protocol | TCP, UDP |
| Ports | Which applications are communicating |
| TCP Flags | Connection state (SYN, ACK, FIN, etc.) |

