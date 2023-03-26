import requests

# ASCII art for Raven banner
print('''
██╗██████╗ ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗     
██║██╔══██╗██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗    
██║██████╔╝██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝    
██║██╔═══╝ ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝     
██║██║     ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║         
╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝         
Made By Tou                                                                                                                                  
''')

def get_location_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        print("IP Address: ", result['ip'])
        print("Country: ", result['country'])
        print("Region: ", result['region'])
        print("City: ", result['city'])
        print("Coordinates: ", result['loc'])
        print("ISP: ", result['org'])
        print("Timezone: ", result['timezone'])
    else:
        print("Error retrieving information")

def check_vpn(ip):
    url = f"https://vpnapi.io/api/{ip}?key=51b22a551fde480da46330c83ea8c0c3"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result['security']['vpn'] == True:
            print("This IP address is detected with a VPN.")
        elif result['security']['proxy'] == True:
            print("This IP address is detected with a proxy.")
        else:
            print("This IP address is not detected with a VPN or proxy.")
    else:
        print("Error retrieving information please contact us via facebook for bug")

def get_my_ip():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    if response.status_code == 200:
        print("Your IP address is:", response.text)
    else:
        print("Error retrieving your IP address")


print("Select an option:\n1. IP lookup\n2. VPN/proxy detection\n3. Get my IP address")
option = input("Enter your choice: ")
if option == "1":
    ip = input("Enter an IP address to lookup: ")
    get_location_info(ip)
elif option == "2":
    ip = input("Enter an IP address to check for VPN/proxy: ")
    check_vpn(ip)
elif option == "3":
    get_my_ip()
else:
    print("Invalid option selected.")

    
