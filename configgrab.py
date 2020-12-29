from netmiko import ConnectHandler

rtr1 = {
    'device_type': 'cisco_xe',
    'ip': '10.10.20.175',
    'username': 'cisco',
    'password': 'cisco', 
}

rtr2 = {
    'device_type': 'cisco_xe',
    'ip': '10.10.20.176',
    'username': 'cisco',
    'password': 'cisco', 
}

nx1 = {
    'device_type': 'cisco_nxos',
    'ip': '10.10.20.177',
    'username': 'cisco',
    'password': 'cisco', 
}

nx2 = {
    'device_type': 'cisco_nxos',
    'ip': '10.10.20.178',
    'username': 'cisco',
    'password': 'cisco', 
}

with open('audit_commands') as c:
    lines = c.read().splitlines()
print (lines)

all_devices = [rtr1, rtr2, nx1, nx2]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(lines)
    print(output)