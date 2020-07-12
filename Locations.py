from urllib.request import urlopen
import json
import re
import requests
import html2text

def getPublicIP():
    data = requests.get('http://checkip.dyndns.com/').content
    ip=html2text.html2text(data.decode("utf-8"))
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(ip).group(1)

IP = str(getPublicIP())

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Print Extracted Details
print ("Your City : " + city)
print ("Your Region : " + region)
print ("Your Country : " + country)
print ("Your Location : " + location)
print ("Your ISP : " + org)

