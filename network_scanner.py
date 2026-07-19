import socket

print("=== simple port Scanner ===")

target = input("enter an ip address: ")

common_ports = [22, 80, 443]

for port in common_ports :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"port {port}: CLOSED")

        sock.close()