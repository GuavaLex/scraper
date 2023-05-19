import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extrator = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extrator.extract(source)["tours"]
    return value

def send_email():
    print("Email Sent")

def store(extracted):
    with open("data.txt","a") as file:
        file.write(extracted + "/n")

def read(extracted):
    with open("data.txt","r") as file:
        return file.read()

if __name__=="__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email()
