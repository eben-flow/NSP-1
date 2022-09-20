from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
from time import sleep



try:
    email = input("Enter the email address to which you would like to receive the automated email\n")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get("https://www.gmail.com")

    driver.find_element_by_id("identifierId").send_keys("papumonu98@gmail.com");
    driver.find_element_by_id("identifierNext").click()
    sleep(3)
    driver.find_element_by_xpath("//div[@id='password']/div[1]/div/div[1]/input").send_keys("PapuMonu98@@")
    driver.find_element_by_id("passwordNext").click()

    sleep(4)
    driver.find_element_by_xpath("""/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div""").click()
    sleep(4)
    driver.switch_to_active_element().send_keys(email)
    # driver.find_element_by_xpath("""//div[@name='to']/div/div[3]/div/div/div/div/div/input""").send_keys("ebenps24@gmail.com")
    driver.find_element_by_xpath("""//input[@name='subjectbox']""").send_keys("TEST\t")
    driver.switch_to_active_element().send_keys("This is an automated email\t")
    driver.switch_to_active_element().click()


except Exception as e:
    print(e)
finally:
    sleep(2000)
    driver.quit()
