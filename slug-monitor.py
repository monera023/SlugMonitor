import json
import time
import random
from datetime import datetime
import requests
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M")

headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

shoeSlugs = []
newShoeSlugs = []
shoeSlugFilePath = "/opt/slug-monitor/shoeSlugs.txt"
diffFilePath = "/opt/slug-monitor/diffSlugs.txt"

urls =  [
    "https://api.nike.com/product_feed/threads/v3/?anchor=0&count=50&filter=marketplace%28IN%29&filter=language%28en-GB%29&filter=inStock%28true%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29",
    "https://api.nike.com/product_feed/threads/v3/?anchor=50&count=50&filter=marketplace%28IN%29&filter=language%28en-GB%29&filter=inStock%28true%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29",
    "https://api.nike.com/product_feed/threads/v3/?anchor=100&count=50&filter=marketplace%28IN%29&filter=language%28en-GB%29&filter=inStock%28true%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29",
    "https://api.nike.com/product_feed/threads/v3/?anchor=150&count=50&filter=marketplace%28IN%29&filter=language%28en-GB%29&filter=inStock%28true%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29"
  ]


def getSlugs(url):
    print("In getSlugs..")
    apiReq = requests.get(url,headers=headers)
    apiInfo = json.loads(apiReq.text)
    apiObjects =  apiInfo['objects']
    return apiObjects


def readSlugsFromFile():
    print("Reading for file..")
    with open(shoeSlugFilePath, "r") as file:
        for line in file.readlines():
            shoeSlugs.append(line.strip())

def writeSlugsToFile(toWriteSlugs):
    print("Writing slugs to file..")
    with open(shoeSlugFilePath, "w") as file:
        for slug in toWriteSlugs:
            file.write(slug + "\n")


def populateSlugs(populateNew):
    print("In populateSlugs")
    
    for url in urls:
        objects = getSlugs(url)
        for item in objects:
            if(populateNew):
                newShoeSlugs.append(item['publishedContent']['properties']['seo']['slug'])
            else:
                shoeSlugs.append(item['publishedContent']['properties']['seo']['slug'])


def writeDiff(diffSet):
    with open(diffFilePath, "a") as file:
        file.write("Found diff on..." + str(formatted_datetime) + "\n")
        for diff in diffSet:
            file.write(diff + "\n")



print("Starting at.." + str(formatted_datetime))
if __name__ == "__main__":
    readSlugsFromFile()
    print("Read slugs for file.." + str(len(shoeSlugs)))
    if(len(shoeSlugs) == 0):
        print("Didn't find old slugs in file..")
        populateSlugs(False)
    
    print("Reading new slugs..")
    populateSlugs(True)
    # writeSlugsToFile(shoeSlugs)
    diffSlugs = set(newShoeSlugs) - set(shoeSlugs)
    diffLen = len(diffSlugs)
    if(diffLen > 0):
        print("Found diff.." + str(diffLen))
        writeDiff(diffSlugs)
    else:
        print("No diff")
    writeSlugsToFile(newShoeSlugs)    
