
from netmiko import ConnectHandler
from getpass import getpass


username = str(input("Enter your username: "))
password = getpass()

with open("cli.txt") as f:
    commands_to_send = f.read().splitlines()
# netmiko.ConnectHandler-----> takes four parameters: ip, device_type, username, and password...so I have included all of them in the dictionary...

ios_device = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.5",
    "username": username,
    "password": password,
}

ios_device2 = {

     "ip": "192.168.10.10",
     "device_type": "cisco_ios",
     "username": username,
     "password": password,

}

ios_device3 = {

     "ip": "192.168.10.20",
     "device_type": "cisco_ios",
     "username": username,
     "password": password,

}


all_devices = [ios_device, ios_device2, ios_device3]   # to include all the devices and their parameters in the form of the list....

for devices in all_devices:                            # to use for loop to iterate through the items inside the list named all_devices
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send)
    output2 = net_connect.send_command("show ip int brief")
    print (output)
    

