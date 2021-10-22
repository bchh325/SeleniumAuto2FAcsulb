from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

with open('autofill.txt') as myFile:
    for line in myFile:
        if '@' in line:
            email = line
        else:
            pw = line

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\BryanPC\\Desktop\\User Data")
options.add_argument("--profile-directory=Profile 2")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=r'C:\Users\BryanPC\Desktop\CSULB\Semester 2\chromedriver.exe', options=options)

driver.get("https://messages.google.com/web/conversations")
driver.execute_script("window.open('https://sso.csulb.edu','_blank');")


driver.switch_to.window(driver.window_handles[1])

time.sleep(2.5)
try:
    emailField = driver.find_element_by_id("i0116")
    emailField.send_keys(email)
except:
    clickEmail = driver.find_element_by_class_name("table")
    clickEmail.click()

time.sleep(2)

passwordField = driver.find_element_by_id("i0118")
passwordField.send_keys(pw)

try:
    signInButton = driver.find_element_by_id("idSIButton9")
    signInButton.click()
except:
    pass

driver.switch_to.window(driver.window_handles[0])
time.sleep(5.5)
unreadMessage = driver.find_element_by_xpath("//mws-conversation-snippet").text

code = ""

for char in unreadMessage:
    if char.isdigit() == True:
        code += char

driver.switch_to.window(driver.window_handles[1])
oneTimeCode = driver.find_element_by_name("otc")
oneTimeCode.send_keys(code)
oneTimeCode.send_keys(Keys.ENTER)








