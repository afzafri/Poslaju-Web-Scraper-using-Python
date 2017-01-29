from selenium import webdriver

trackNo = "YOUR_TRACKING_NUMBER"

path_to_chromedriver = 'C:\driver\chromedriver.exe' # Path to the chromedriver. change path as needed.
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'http://poslaju.com.my/track-trace-v2/' # poslaju tracking website URL
browser.get(url) # open the browser and load the website

# find the textarea html element using its ID
textarea = browser.find_element_by_id('trackingNo03')
textarea.clear() # clear the form field
textarea.send_keys(trackNo) # send the tracking number to the form

browser.find_element_by_id('bttest').click() # find the submit button, and click it