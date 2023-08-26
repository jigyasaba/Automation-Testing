from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
options=Options()
options.add_experimental_option("detach", True)#will keep the browser open even after the task is done
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/maps/")
driver.maximize_window()# For maximizing window
print("Welcome to "+driver.title)#title of the page
sleep(2)
def searchplace():
    #destination=input("Helooo..Please enter your  Destination")
    PLACE=driver.find_element("xpath","/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input")
    PLACE.send_keys("Uttarkhand")
    driver.find_element("xpath","/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button").click()
searchplace()
def directions():
    sleep(10)
    driver.find_element("xpath","/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span").click()
directions()

def find():
    sleep(8)
    destination=driver.find_element("xpath","/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    destination.send_keys("Punjab")
    sleep(8)
    driver.find_element("xpath","/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]").click()
find()
print("PUNJAB TO UTTARAKHAND")
def distance1():
   sleep(8)
   Total=driver.find_element("xpath","/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]")
   print("Total kilometeres : ",Total.text)
   sleep(8)
   Bus=driver.find_element("xpath","/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[2]/div[1]/div/div[1]/div[1]")
   print("Bus  Travel will take: "+Bus.text)
   sleep(8)
   Twowheeler=driver.find_element("xpath","/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[1]")
   print("Two wheeler will take around: "+Twowheeler.text)
distance1()




