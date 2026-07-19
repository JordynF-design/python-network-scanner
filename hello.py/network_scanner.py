print("=== Simple Network scanner ===")

target = input("Enter an IP address: ")
print("Scanning:", target)
common_ports = [22, 80, 443]
for port in common_ports:
    print(f"Cheaking port{port}...")
    