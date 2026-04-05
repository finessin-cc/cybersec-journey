import socket
SERVICES = {
    21: "FTP", 22: "SSH", 25: "SMTP",
    53: "DNS", 80: "HTTP", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

target = input("Enter target: ")
ports = [21, 22, 25, 53, 80, 443, 3306, 3389, 8080]

print(f"\nScanning {target}...")
print("─" * 40)

for port in ports:
    service = SERVICES.get(port, "Unknown")
    if check_port(target, port):
        print(f"[OPEN]   port {port} → {service}")
    else:
        print(f"[closed] port {port} → {service}")
