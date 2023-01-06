import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

browser = webdriver.Chrome(options=options, executable_path=r'/mnt/c/Program\ Files/Google/Chrome/Application/chrome.exe --incognito')
#browser.manage().timeouts().implicitlyWait(50);
browser.implicitly_wait(10)
browser.get("https://www.fitnessworld.com/dk2/")
print("Getting Web Page!")
try: 
    
    cookiepolicy_elem = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'coi-banner__accept')))
    cookiepolicy_elem.click()
    time.sleep(2)
    
    login = browser.find_element(By.CLASS_NAME, "header__login")

    browser.execute_script("arguments[0].scrollIntoView(true);", login);
    browser.execute_script("arguments[0].click();", login);
    time.sleep(2)
    loginForm = browser.find_element(By.ID, "user-login-form")
    loginInput = loginForm.find_element(By.ID, "edit-name")
    passInput = loginForm.find_element(By.ID, "edit-pass")
    
    loginInput.send_keys("friistyler@gmail.com")
    passInput.send_keys("rBh8wkMrzPG5A44")

    browser.save_screenshot('form.png')
    submit_elem = loginForm.find_element(By.ID, "edit-submit")
    submit_elem.submit()
    time.sleep(5)
    browser.get("https://www.fitnessworld.com/dk2/holdtraening")
    time.sleep(5)
    browser.save_screenshot('hold.png')
    now = datetime.now().strftime("%Y-%m-%d")
    month = (datetime.now() + timedelta(days=21)).strftime("%Y-%m-%d")
    #browser.get("https://www.fitnessworld.com/dk2/api/search_activities?classes%5B%5D=35541&centers%5B%5D=114&from=2022-12-22&to=2023-01-12")
    browser.get("https://www.fitnessworld.com/dk2/api/search_activities?classes[]=35541&centers[]=114&from="+now+"&to="+month+"")
    result = browser.find_element_by_tag_name('pre').text
    browser.save_screenshot('screenshot.png')

except Exception as ex:
    print(ex)

finally:
    browser.quit()