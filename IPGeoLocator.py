import urllib, json
import urllib.request

def locate(ip):
    with urllib.request.urlopen(f"https://ipinfo.io/{ip}/json") as url:
        data = json.load(url)
        if "ip" in data:
            print("IP Address:",data["ip"])    
        if "city" in data:
            print("City:",data["city"])
        if "region" in data:
            print("Region:",data["region"])
        if "country" in data:
            print("Country:",data["country"])
        if "postal" in data:
            print("Zip Code:",data["postal"])
        if "timezone" in data:
            print("Timezone:",data["timezone"])
        if "hostname" in data:
            print("Hostname:",data["hostname"])
        if "loc" in data:
            print("Coorinates:",data["loc"])
        if "org" in data:
            print("Org:",data["org"])

while(True):
    iploc = str(input("Please enter the IP Address to Geolocate: "))
    locate(iploc)
