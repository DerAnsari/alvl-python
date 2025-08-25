from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your web driver (e.g., ChromeDriver)
driver_path = 'path/to/chromedriver'

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Open YouTube
driver.get('https://www.youtube.com/')

# Wait for page to load (you can adjust the time as needed)
time.sleep(3)

# Find the comment section (XPath used as an example)
comment_section = driver.find_element_by_xpath('//*[@id="comments"]')

# Scroll to the comment section
comment_section.location_once_scrolled_into_view

# Wait for page to scroll (optional)
time.sleep(2)

# Find the comment input field and submit a comment
comment_input = driver.find_element_by_xpath('//*[@id="placeholder-area"]')
comment_input.send_keys('This is a test comment.')
comment_input.send_keys(Keys.RETURN)

# Wait for comment to be submitted (optional)
time.sleep(2)

# Close the browser
driver.quit()
