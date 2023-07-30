from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Required when running as root user
driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:8000/")
print(driver.title)
time.sleep(10)  # Reduced the sleep time for demonstration purposes
driver.quit()
