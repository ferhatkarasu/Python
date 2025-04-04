### Subnet Calculator

x=input("IP address and Prefix -> Example: 192.168.1.1/24\n==>")
ip,str_prefix_length=x.split("/")
prefix_length=int(str_prefix_length)


def calculate_subnet_mask(prefix_length):
    mask = (1 << 32) - (1 << (32 - prefix_length))
    subnet_mask = [(mask >> (8 * (3 - i))) & 255 for i in range(4)]
    return '.'.join(map(str, subnet_mask))

subnet_mask = calculate_subnet_mask(prefix_length)



def calculate_network_address(ip,subnet_mask):
    ip_part=list(map(int, ip.split(".")))
    subnet_part=list(map(int,subnet_mask.split(".")))

    network_address=[ip_part[i] & subnet_part[i] for i in range(4)]
    return '.'.join(map(str, network_address))

network_address=calculate_network_address(ip,subnet_mask)



def calculate_broadcast_address(ip, subnet_mask):
    ip_part = list(map(int, ip.split(".")))
    subnet_part = list(map(int, subnet_mask.split(".")))
    
    broadcast_parts = [
        (ip_part[i] | (255 - subnet_part[i])) for i in range(4)
    ]
    return '.'.join(map(str, broadcast_parts))

broadcast_address = calculate_broadcast_address(ip, subnet_mask)


def calculate_usable_range(network_address,broadcast_address):
    network_parts = list(map(int, network_address.split('.')))
    broadcast_parts = list(map(int, broadcast_address.split('.')))
    
    usable_start = '.'.join(map(str, [network_parts[0], network_parts[1], network_parts[2], network_parts[3] + 1]))
    usable_end = '.'.join(map(str, [broadcast_parts[0], broadcast_parts[1], broadcast_parts[2], broadcast_parts[3] - 1]))    
    return usable_start, usable_end
  
usable_start, usable_end = calculate_usable_range(network_address, broadcast_address)



print("IP Address: ",ip)
print("Prefix: /",prefix_length)
print("Network Adress: ",network_address)
print("Subnet Mask: ", subnet_mask)
print("Broadcast Address: ",broadcast_address)
print("Usable Host IP Range: ",usable_start,"-", usable_end)
