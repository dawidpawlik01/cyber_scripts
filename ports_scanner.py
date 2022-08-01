from operator import countOf
import socket


def scan(target,ports):
    for port in range(1, ports):
        scan_port(target, port)
        
    if port in opened_ports:
      print(f' There is a list of opened ports {opened_ports}')
    print("[ 0 PORTS FOUND ] There is no opened ports")      
    #print(f'There is a list of closed ports {closed_ports}') 

def scan_port(ipaddr, port):
    try:
        sckt = socket.socket()
        sckt.connect((ipaddr, port))
        opened_ports.append(port)
        sckt.close()
        
    except:
       # closed_ports.append(port)
       pass
        
        

target = input("Enter IP Addres Target ( you can split a range of adresses  by , ): ")
ports = int(input("Enter a count of ports you want to scan : "))
opened_ports = []
closed_ports = []

if ',' in target: 
    print("Scanning multiple targets")
    for ip_addr in target.split(','):
        scan(ip_addr.strip(' '), ports)
else: 
    scan(target, ports)        
            
