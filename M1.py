import pyperclip
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

file_path = "Top Comps.txt"


subprocess.Popen(["notepad.exe", file_path])
# Start browser
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
# Open website
driver.get("https://tactics.tools")
time.sleep(random.uniform(0.5, 1.5))
# Find input field and type
STATS = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'STATS'))
)
time.sleep(random.uniform(0.5, 1.5))
STATS.click()
codes = []
wait = WebDriverWait(driver, 10)

# Wait until at least one button exists
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "button[aria-label='Copy Team Planner code']")
    )
)
Comps = driver.find_elements(
    By.CSS_SELECTOR,
    "button[aria-label='Copy Team Planner code']"
)

Used_Codes = set()

while True:
    Comps = driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Copy Team Planner code']")
    new_comp = False
    for comp in Comps:
        comp_id = comp.id
        if comp_id in Used_Codes:
            continue
        new_comp = True
        Used_Codes.add(comp_id)
        driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", comp)  
        try:
            comp.click()
        except Exception:

            driver.execute_script("arguments[0].click();", comp)  
        

        time.sleep(random.uniform(0.5, 1.5))
        
        try:
            alert = driver.switch_to.alert
            print("Alert detected, Waiting for Manual Click")

            while True:
                time.sleep(1)
                try:
                    alert.text  # Check if alert is still present
                except Exception:
                    print("Alert closed, Resuming")
                    break
        except:
                pass
        

       
        time.sleep(random.uniform(0.5, 1.5))  # Wait for clipboard update

        code = pyperclip.paste()
        codes.append(code)

        
    if not new_comp:
        break
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(random.uniform(0.5, 1.5))

with open(file_path, "w") as f:
    for code in codes:
        f.write(code + "\n")


time.sleep(3)

# Close browser
driver.quit()