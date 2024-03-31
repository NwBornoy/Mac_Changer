#!/usr/bin/env python
import re
import subprocess
import optparse
def g_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Eth0 ni mac o'zgartirish")
    parser.add_option("-m", "--mac", dest="new_mac", help="Eth0 ni mac o'zgartirish")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("interfase ni kiriting yoki -- halp niyozing!")
    elif not option.new_mac:
        parser.error("new_mac ni kiriting yoki -- help ni yozing!")
    return option
def change_mac(interface, new_mac):
    interface = interface
    new_mac = new_mac
    print(type(interface))
    print(type(new_mac))
    print(" [+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def get_current(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    print(type(ifconfig_result))

    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode())
    if mac_address:
        return mac_address.group(0)
    else:
        print("[-]Mac manzil topilmadi:")



option= g_arguments()
mac_current = get_current(option.interface)
print(" mac address", str(mac_current))

change_mac(option.interface, option.new_mac)
mac_current = get_current(option.interface)
if mac_current == option.new_mac:
    print("Mac manzil o'zgardi: " + mac_current )
else:
    print("Manzil o'zgarmagan: ")


