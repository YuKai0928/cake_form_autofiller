from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
web = webdriver.Chrome()
url = 'https://www.surveycake.com/s/ZZVAK' #Fake one
name = 'chen Ding'
ID = 'h1029993891'
birth = '0229'
phone = '0911022999'
web.get(url)
opened = False
times = 1
while(1):
	while(1):
		while(1):
			try:
				not_open = web.find_element_by_xpath('//*[@id="survey"]/div/div/div/div/div/h2')
				print('not opened')
				break
			except:
				try:
					texts = web.find_elements_by_css_selector("[data-qa='subject-type-TXTSHORT']")
					A = texts[0]
					print('opened')
					opened = True
					break
				except:
					pass
		if(opened):
			break
		print('refreshed',times)
		web.refresh()
		times+=1
	body = web.find_element_by_tag_name('body')
	while(1):
		try:
			print('fetching txt blocks')
			texts = web.find_elements_by_css_selector("[data-qa='subject-type-TXTSHORT']")
			break
		except:
			pass
	while(1):
		try:
			print('trying')
			texts[0].send_keys(name)
			break
		except:
			pass
	while(1):
		try:
			print('trying')
			web.find_element_by_css_selector("[data-qa='option-男生']").click()
			break
		except:
			pass
	while(1):
		try:
			print('trying')
			texts[1].send_keys(ID)
			break
		except:
			pass
	while(1):
		try:
			print('trying')
			texts[2].send_keys(birth)
			break
		except:
			pass
	body.send_keys(Keys.PAGE_DOWN)
	while(1):
		try:
			print('trying')
			texts[3].send_keys(phone)
			break
		except:
			pass
	while(1):
		try:
			print('trying')
			time.sleep(0.2)
			web.find_element_by_css_selector("[data-qa='option-第一季']").click()
			break
		except:
			continue
	while(1):
		try:
			print('trying')
			time.sleep(0.2)
			web.find_element_by_css_selector("[data-qa='option-否']").click()
			break
		except:
			continue
	
	while(1):
		try:
			print('trying')
			time.sleep(0.2)
			web.find_element_by_css_selector("[data-qa='submit']").click()
			break
		except:
			continue
	break