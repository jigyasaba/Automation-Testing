from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
options=Options()
options.add_experimental_option("detach", True)#will keep the browser open even after the task is done
driver = webdriver.Chrome(options=options)
driver.get("https://www.neuralnine.com/")
driver.maximize_window()# For maximizing window
print(driver.title)#title of the page
print(driver.current_url)
links=driver.find_elements("xpath","//a[@href]")#gives me all the anchor tags that have @href attribute i.e.,basicallly the link
for link in links:
   #print(link.get_attribute("innerHTML"))#whatever is inside of the anchor tag will get printed
   if "Books" in link.get_attribute("innerHTML"):
     link.click()
     break
book_links=driver.find_elements("xpath","//div[contains(@class,'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")
#for book_link in book_links:
    #print(book_link.get_attribute("href"))
book_links[0].click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
buttons=driver.find_elements("xpath","//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")
for button in buttons:
    print(button.get_attribute("innerHTML"))
#driver.find_element(By.ID,"searchField").send_keys("Movies")
#driver.find_element(By.NAME,"q").send_keys("youtube")
#driver.find_element(By.NAME,"btnK").click()
#driver.implicitly_wait(20)

#driver.find_element(By.NAME,"btnGNS").send_keys("rinnisgarden")
#driver.find_element(By.NAME,"btnGNS").click()



#time.sleep(5)
# print(driver.page_source) prints the html code of the web page
# driver.find_elements_by_id('searchField').send_keys('movies')

