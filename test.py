from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Required when running as root user
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://127.0.0.1:8000/")
    print("Page title:", driver.title)
except Exception as e:
    print("Error accessing the page:", e)

# Add this line to make sure the WebDriver is properly closed
driver.quit()
