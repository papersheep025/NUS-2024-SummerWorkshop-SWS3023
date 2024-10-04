# @FileName  :next_page.py
# @Time      :2024/7/10 14:06
# @Author    :Papersheep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary  # For the chromedriver binary path

# Initialize WebDriver
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("window-size=600,800")
driver = webdriver.Chrome()

def go_to_next_page():
    # Open target page
    driver.get("https://www.yelp.com/search?find_desc=Restaurants&find_loc=Singapore")

    try:
        # Locate the "Next Page" button
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.pagination-button__09f24__kbFYf.y-css-1ewzev[data-button="true"]'))
        )
        # Click the button
        button.click()
        print("Clicked 'Next Page' button.")

        # Optionally wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'span.y-css-5h56mr[disabled]'))
        )

    except Exception as e:
        print(f"An error occurred: {e}")

# Example function call
go_to_next_page()

# Close the browser
driver.quit()


if __name__ == "__main__":
    run_code = 0
