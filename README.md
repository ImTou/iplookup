# IP Lookup and VPN/Proxy Detection  ![](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <img src="https://komarev.com/ghpvc/?username=TheRealTou&color=brightgreen" alt="watching_count" />
![](https://media.discordapp.net/attachments/1028720953515057162/1028914619219181609/vector.png)
This tool provides two functions: IP lookup and VPN/proxy detection. It uses the requests library in Python to send HTTP requests to the ipinfo.io and vpnapi.io APIs.

* Follow me on Facebook
For more information about me and my other projects, you can follow me on Facebook
[![Facebook](https://img.shields.io/badge/Follow-Facebook-blue)](https://www.facebook.com/)

## Installation
### Linux
```
git clone https://github.com/TheRealTou/iplookup
pip install requests
cd iplookup
python iplookup.py
```
### Window
* First, download the iplookup.py file to your computer.
* Install Python on your computer if you haven't already. You can download it from the official Python website: https://www.python.org/downloads/
* Install the requests library. You can do this by running the following command in your terminal or command prompt:
```python
pip install requests
```
* Open your terminal or command prompt and navigate to the directory where you saved the iplookup.py file.
* Run the iplookup.py file by typing the following command and pressing enter:
```
python iplookup.py
```

## Help Guide
```
$ python ip_lookup.py
  _____    ___     __  __ ____
 ██╗██████╗ ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗     
██║██╔══██╗██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗    
██║██████╔╝██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝    
██║██╔═══╝ ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝     
██║██║     ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║         
╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝         
Made By Tou 

Select an option:
1. IP lookup
2. VPN/proxy detection
3. Get my IP address
Enter your choice: 1
Enter an IP address to lookup: 8.8.8.8
IP Address:  8.8.8.8
Country:  US
Region:  California
City:  Mountain View
Coordinates:  37.3860,-122.0838
ISP:  AS15169 Google LLC
Timezone:  America/Los_Angeles
```
* If VPN/proxy error just change api to your api get api from: https://vpnapi.io/
```python
def check_vpn(ip):
    url = f"https://vpnapi.io/api/{ip}?key=YOUR-API" 
```

## Credits
This tool was made by Tou using the vpnapi.io APIs.

## Disclamier
This tool is provided for educational and informational purposes only. The accuracy and reliability of the information provided by this tool are not guaranteed. The tool is provided "as is" without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.
