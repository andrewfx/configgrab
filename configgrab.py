from netmiko import ConnectHandler

rtr1 = {
    'device type': 'cisco_xe',
    'ip': 'x.x.x.x',
    'username': 'cisco',
    'password': 'cisco', 
}

rtr2 = {
    'device type': 'cisco_xe',
    'ip': 'x.x.x.x',
    'username': 'cisco',
    'password': 'cisco', 
}

nx1 = {
    'device type': 'cisco_nxos',
    'ip': 'x.x.x.x',
    'username': 'cisco',
    'password': 'cisco', 
}

nx2 = {
    'device type': 'cisco_nxos',
    'ip': 'x.x.x.x',
    'username': 'cisco',
    'password': 'cisco', 
}

with open('audit_commands') as c:
    lines = c.read().splitlines()
print(lines)

all_devices = [rtr1, rtr2, nx1, nx2]

for device in all_devices
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(lines)
    print(output)