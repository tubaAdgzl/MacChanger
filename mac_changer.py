import re
import subprocess
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="use for change your interface")
    parse_object.add_option("-m","--mac",dest="mac_address",help="use for change your mac address")

    return parse_object.parse_args()

def change_mac(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("**WELCOME MacChanger** \n --MacChanger started--!")

(input,arguments) = get_user_input()
change_mac(input.interface,input.mac_address)
mac = control_new_mac(str(input.interface))

if mac == input.mac_address:
    print("-*Your mac address has been changed by MacChanger!*-")
else:
    print("Error:Somethings went wrong!")