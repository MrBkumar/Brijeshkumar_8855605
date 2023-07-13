from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Initialize the WebDriver with incognito mode
driver = webdriver.Chrome(options=chrome_options)

# Open YouTube
driver.get("https://www.youtube.com/")

# Search for a Selenium with python tutorial
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Selenium with python")
search_box.submit()

# Wait for the search results page to load
time.sleep(2)

# Click on the first video in the search results
first_video = driver.find_element(By.CSS_SELECTOR, "#contents ytd-video-renderer")
first_video.click()

# Wait for the video to start playing
time.sleep(5)
start_time = time.time()

# Skip ads
time.sleep(5)
skip_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[18]/div/div[3]/div/div[2]/span")
skip_button.click()

# Wait for the video to play for a 15 seconds
time.sleep(15)

# Close the browser
driver.quit()