from netmiko import ConnectHandler

#function which prints the collected output
def configoutput():
    print("======== Int status of " + name + " =========")
    print(output)
    print("=============== CONFIG END ===============")

#list of network devices to connect to
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
    n = net_connect.send_command('show run | sec hostname')
    name = n.strip('hostname \n')
    output = net_connect.send_command('show ip int brief')

    configoutput()

#write output to file
    file = open(name, "w")
    file.write(output)
    file.close()
