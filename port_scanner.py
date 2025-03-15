import socket
import threading

# Target to scan
target = input("Enter target host (IP/Domain): ")

# Resolve IP address from hostname (if domain given)
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Could not resolve hostname.")
    exit()

print(f"Scanning target: {target} ({target_ip})")

#Ports to scan (common ports)
port_range = range(1, 1025)

#Function to scan single port
def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1) # 1 second timeout
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is open.")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Scan ports using threading for concurrency
def start_scan():
    threads = []

    for port in port_range:
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Scanning completed.")

if __name__=="__main__":
    start_scan()
