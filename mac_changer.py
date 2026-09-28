#!/usr/bin/env python 

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest="interface", help="Interface to change it MAC Address")
    parser.add_option('-m', '--mac', dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        #Code to handle error
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        #Code to handle error
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    return options

        

def change_mac(interface, new_mac):
  
    print("[+] Changing MAC Address for " + interface + " to : " + new_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_result:
        return mac_address_result.group(0)
    else:
        return None
    print("[-] Could not read MAC Address...")



options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC Address: " + str(current_mac))

change_mac(options.interface, options.new_mac)


current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[*] MAC Address was successfully changed to " + str(current_mac))
else:
    print("[-] MAC Address did not get changed.")