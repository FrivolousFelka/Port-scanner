import socket
import threading

target_host = input("Host:")
start_port = input("Starting Port:")
end_port = input("End Port:")

start_port = int(start_port)
end_port = int(end_port)

print_lock = threading.Lock()


def scan_ports(port):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)

    try:
        result = client.connect_ex((target_host, port))
        if result == 0:
            with print_lock:
                print(f"Port {port}: Open")
    except socket.error:
        with print_lock:
            print(f"Port {port}: Error occurred")

    client.close()


for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_ports, args=(port,))
    thread.start() 
    
    
input("Scan Finished Press Anything To Continue")
