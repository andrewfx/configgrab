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

all_devices = [rtr1, rtr2, nx1, nx2]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    name = net_connect.send_command('show run | sec hostname')
    output = net_connect.send_command('terminal length 0')
    output = net_connect.send_command('show ip int brief')
    print("==== Interface Status of " + name.strip('hostname ') + " ===== ")
    print(output)
    print("=============== CONFIG END ===============")
        