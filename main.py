# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
# driver = webdriver.Chrome("C:/Users/inbals/Downloads/programs/chromedriver.exe")
# driver.get("https://stackoverflow.com/questions/34256762/error-could-not-find-a-version-that-satisfies-the-requirement-webdriver-from")

import requests
import re
from bs4 import BeautifulSoup


def first_attempt():
    url = "https://alcohol123.co.il/product/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99-%d7%91%d7%9c%d7%95%d7%95%d7%99%d7%a0%d7%99-14-%d7%a7%d7%90%d7%a8%d7%99%d7%91%d7%99%d7%90%d7%9f-%d7%a7%d7%90%d7%a1%d7%a7/"
    # url = "https://alcohol123.co.il/product/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99-%d7%92%d7%9c%d7%a0%d7%9c%d7%99%d7%95%d7%95%d7%98-12-%d7%a9%d7%a0%d7%94-700-%d7%9e%d7%9c/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    data_from_page(soup)
    # name = soup.find('h1', class_=re.compile("product_title"))
    # print("name: " + name.text)
    #
    # price = soup.find('p', class_=re.compile("price"))
    # print("price: " + price.text)
    #
    # volume = soup.find('span', id=re.compile("lblItemVolumePer100ml"))
    #
    # print("volume: " + volume.text)
    # # print(soup.find('span'))
    # # print(soup.find_all('td', id=re.compile("rptFeatureTemplateFieldsBelowPic")))
    # f = soup.find_all('td', id=re.compile("rptFeatureTemplateFieldsBelowPic"))
    #
    # print(f[1])
    # print(soup.find('span', 'aria-label'=re.compile("שם יצרן")))


def data_from_page(soup):
    name = soup.find('h1', class_=re.compile("product_title"))
    print("name: " + name.text)

    price = soup.find('p', class_=re.compile("price"))
    print("price: " + price.text)

    # volume = soup.find('span', id=re.compile("lblItemVolumePer100ml"))
    # print("volume: " + volume.text)

    # print(soup.find('div', id=re.compile("quantityAndPurchaseButtonsWrapper")))
    available = soup.find('button', class_=re.compile("add_to_cart_button"))
    if not available:
        print("outOfStock")

    # cont = soup.find_all('section', class_=re.compile("elementor-section-full_width"))
    # cont[0].
    # print(cont)
    #
    # def h2fromcont(container):
    #     container.find_all()
    # h2 = map(h2fromcont, cont)
    # print(soup.find('span'))
    # print(soup.find_all('td', id=re.compile("rptFeatureTemplateFieldsBelowPic")))
    # f = soup.find_all('td', id=re.compile("rptFeatureTemplateFieldsBelowPic"))

    # print(f[1])
    # print(soup.find('span', 'aria-label'=re.compile("שם יצרן")))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


from the_importer import TheImporter
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #first_attempt()
    # importer = TheImporter()
    # print("-------------------גורדונס---------------------")
    # # search_attempt('גורדונס')
    # print("-------------------טרי אוליבס---------------------")
    # search_attempt('טרי אוליבס')
    # print("-------------------kalua---------------------")
    # importer.search_attempt('קלואה')
    # print("-------------------ג'יימסון---------------------")
    # importer.search_attempt("ג'יימסון")
    # importer.search_attempt("ג'יימסון סלקט רזרב")
    # print("-------------------ג'ק דניאלס---------------------")
    # importer.search_attempt("ג'ק דניאלס")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
