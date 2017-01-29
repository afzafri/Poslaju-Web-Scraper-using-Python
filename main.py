from selenium import webdriver

trackNo = "YOUR_TRACKING_NUMBER"

path_to_chromedriver = 'C:\driver\chromedriver.exe' # Path to the chromedriver. change path as needed.
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'http://poslaju.com.my/track-trace-v2/' # poslaju tracking website URL
browser.get(url) # open the browser and load the website