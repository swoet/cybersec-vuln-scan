import nmap

def scan_host(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print("State:", nm[host].state())
        for proto in nm[host].all_protocols():
            print("Protocol:", proto)
            for port in sorted(nm[host][proto].keys()):
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Change this as needed
    scan_host(target_ip)
