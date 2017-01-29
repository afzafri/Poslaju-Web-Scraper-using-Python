import sys
import json
from selenium import webdriver

print "------------------------------------------\n"
print "Poslaju Web Scraper by Afif Zafri \nGithub: afzafri \n"
print "------------------------------------------\n"

if len(sys.argv) < 2:

	print "Usage: python main.py <tracking_number>"

else:

	print "Executing script...\n"

	trackNo = sys.argv[1] # your tracking number. received via command line argument

	path_to_chromedriver = 'C:\driver\chromedriver.exe' # Path to the chromedriver. change path as needed.
	browser = webdriver.Chrome(executable_path = path_to_chromedriver)
	url = 'http://poslaju.com.my/track-trace-v2/' # poslaju tracking website URL
	browser.get(url) # open the browser and load the website

	# find the textarea html element using its ID
	textarea = browser.find_element_by_id('trackingNo03')
	textarea.clear() # clear the form field
	textarea.send_keys(trackNo) # send the tracking number to the form

	browser.find_element_by_id('bttest').click() # find the submit button, and click it

	# find the result table
	restable = browser.find_element_by_id('tbDetails')

	print "Results:\n"

	results = {}
	i = 0
	
	# parse each row and column of the table, and print
	for row in restable.find_elements_by_tag_name('tr'):
		column = row.find_elements_by_tag_name('td')
		for j in range(len(column)):
			results[i] = {'datetime' : column[0].text, 'process' : column[1].text, 'event' : column[2].text}

		i = i + 1

	print json.dumps(results, indent=1)