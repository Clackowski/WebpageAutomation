from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Prompt user to enter website name
url = input("Enter url of website: ")
#url = "https://clackowski.github.io/Portfolio/"

# Create a WebDriver instance for Chrome
driver = webdriver.Chrome()

# Open your portfolio website
driver.get(url)

input("Press Enter to begin button pressing script...")

try:
    # Find the first button element on the page using tag name
    buttons = driver.find_elements(By.TAG_NAME, "a")
    for index, button in enumerate(buttons):
        print("Button " + str(index))
        print("Text: " + str(button.text))
        print()

    # Click the button
    #button.click()
    #print("Button clicked successfully!")
except Exception as e:
    print(f"An error occurred: {e}")



# Wait until the user presses Enter to close the browser
input("Press Enter to close the browser...")
driver.quit()