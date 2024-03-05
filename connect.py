# Dominic Minnich 
# (Public connect.py)
# When you run this script, it will connect to the Wi-Fi network with the specified name and password.
# You do need to be connected to the wifi network previously in order to run this script.

# This script is designed to be run on windows for connecting many new or old devices to a wifi network.


# Make sure you change the WIFI_NAME and PASSWORD to your Wi-Fi network name and password!

import subprocess

WIFI_NAME = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

def connect_to_wifi(ssid, password):
    # Create a command string to add the wireless network profile
    command = f'netsh wlan add profile filename="{ssid}.xml"'

    # Create the XML content for the network profile
    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{ssid}</name>
        <SSIDConfig>
            <SSID>
                <name>{ssid}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>{password}</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>'''

    # Write the XML content to a file
    with open(f'{ssid}.xml', 'w') as file:
        file.write(xml_content)

    # Run the command to add the network profile
    subprocess.run(command, shell=True)

    # Create a command string to connect to the Wi-Fi network
    connect_command = f'netsh wlan connect name={ssid}'

    # Run the command to connect to the Wi-Fi network
    subprocess.run(connect_command, shell=True)

# Call the function to connect to the Wi-Fi network
connect_to_wifi(WIFI_NAME, PASSWORD) 

