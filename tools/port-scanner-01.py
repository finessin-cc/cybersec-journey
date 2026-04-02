import socket

target = input("Enter target: ")
ports = [21, 22, 25, 53, 80, 443, 3306, 3389, 8080]

print("Target:", target)
print("Ports to scan:", ports)

for port in ports:
    print("Checking port:", port)
    
SERVICES = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}
    
def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except:
        return False

print("\n--- Scan Results ---")
for port in ports:
    service = SERVICES.get(port, "Unknown")
    if check_port(target, port):
        print(f"[OPEN]   port {port} → {service}")
    else:
        print(f"[closed] port {port} → {service}")