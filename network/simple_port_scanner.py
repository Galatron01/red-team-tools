import socket

targets = input("Enter target IP: ")
ports = [22, 80, 443, 445, 3389]

print(f"\nScanning {targets}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((targets, port))

    if result == 0:
        print(f"[+] Port {port} OPEN")
    else:
        print(f"[-] Port {port} closed")
