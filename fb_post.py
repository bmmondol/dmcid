from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

cookie_raw = os.getenv("FB_COOKIE")
group_link = os.getenv("GROUP_LINK")
post_text = os.getenv("POST_TEXT")

# --- Configure Chrome ---
opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

# Open Facebook
driver.get("https://www.facebook.com")

# Convert cookie string → selenium cookie
if cookie_raw:
    for part in cookie_raw.split("; "):
        key, val = part.split("=", 1)
        driver.add_cookie({"name": key, "value": val})

driver.get(group_link)
time.sleep(5)

# Post Box find
textarea = driver.find_element("xpath", "//div[contains(@aria-label,'Write something')]")
textarea.click()
time.sleep(2)

# Type message
post_box = driver.find_element("xpath", "//div[@role='textbox']")
post_box.send_keys(post_text)
time.sleep(2)

# Click Post Button
post_btn = driver.find_element("xpath", "//div[@aria-label='Post']")
post_btn.click()

time.sleep(5)
driver.quit()

print("Post Successful.")
