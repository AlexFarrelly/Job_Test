# Load selenium moduals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

# Set features to run without a GUI
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

def wait_for_page(driver, id):
    try:
        #waits for a new element with the id specified to generate/appear
        element_present = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, id)))
    except TimeoutException as e:
        wait_for_page(driver, id)

def hyperoptic():
    # Establish chrome driver and go to report site URL
    hyperoptic_url = "https://www.hyperoptic.com/"
    hyperoptic_driver = webdriver.Chrome(options = options)
    hyperoptic_driver.get(hyperoptic_url)
    # Clicking the Accept cookies buttom
    hyperoptic_driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div[3]/button[1]").click()
    # Waiting for the page to load
    wait_for_page(hyperoptic_driver, "contractButton2")
    hyperoptic_driver.find_element_by_xpath("/html/body/div[3]/div[6]/div/div[3]/div/div[2]/div[1]/label[3]").click()
    # Waiting for the page to load
    time.sleep(1) # used time insted of wait function as i wasnt waiting for a change in elemnts
    # Gathering all text in the class named body (body of text)
    items = hyperoptic_driver.find_elements_by_class_name("body")
    info  = [(item.text).split("\n") for item in items]
    # Organising and displaying the text
    deal_names = ["Fast", "Superfast", "Ultrafast", "Hyperfast"]
    titles = ["Deal price:",  "Deal Speed:", "Deal Set Up Cost:", "Deal Contract Length:"]
    print("="*30 +"Hyperoptic Deals"+"="*30)
    for i, deal in enumerate(info):
        print("-"*30+deal_names[i]+"-"*30)
        for index, item in enumerate([0,3,5,1]):
            print(titles[index] +" "+deal[item])
    hyperoptic_driver.quit()
        
def bt(postcode):
    # Establish chrome driver and go to report site URL
    bt_url = "https://www.bt.com/broadband"
    bt_driver = webdriver.Chrome(options = options)
    bt_driver.get(bt_url)
    time.sleep(3)
    # Finding the entry box and entering in the postcode
    postcode_entry = bt_driver.find_element_by_id("sc-postcode")
    postcode_entry.send_keys(postcode)
    # Navigation through address selection screen
    bt_driver.find_element_by_xpath("/html/body/div[1]/div/main/section[2]/div[1]/div[2]/section/div[1]/div/div/div/div/div/div/div/div/form/div/div[2]/div[2]/button").click()
    wait_for_page(bt_driver, "tvsc-address") #wait for menu to appear 
    bt_driver.find_element_by_xpath("/html/body/div[1]/div/main/section[2]/div[1]/div[2]/section/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/form/div[1]/div/select/option[2]").click()
    time.sleep(1) # as no new elements appear the sleep function is needed
    bt_driver.find_element_by_xpath("/html/body/div[1]/div/main/section[2]/div[1]/div[2]/section/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/form/div[2]/button").click()
    # Waiting for the page to load
    wait_for_page(bt_driver, "product-name")
    # Gathering all deal info
    info = [(bt_driver.find_elements_by_id(id)[0].text).split("\n") for id in ["SFFEU", "UINF1-NEW", "UINF2-NEW"]]
    print("\n"+"="*30 +"BT Deals"+"="*30)
    titles = ["Deal price:", "Deal speed:","Deal Set Up Cost:", "Deal Contract Length:"]
    for deal in info:
        print("-"*30+deal[1]+"-"*30)
        deal = deal[2:]
        for title_index, index in enumerate([9,0,11,10]):
            print(titles[title_index]+" "+deal[index])
    bt_driver.quit()
hyperoptic()
bt("IP11 7RZ")
