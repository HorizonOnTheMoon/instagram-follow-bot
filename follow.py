
"""
__Author__ = Ufuk Karabağ
__CopyRight__ = CopyRiht 2021, Planet Earth 

"""



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		
		driver = self.driver
		driver.get("https://instagram.com/")
		time.sleep(2)
		user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		password_elem = driver.find_element_by_xpath("//input[@name='password']")
		password_elem.clear()
		password_elem.send_keys(self.password)
		password_elem.send_keys(Keys.RETURN)
		time.sleep(3)
	def follow_this_users_followers(self, willFollow):
		driver = self.driver
		driver.get("https://www.instagram.com/{}/".format(willFollow))	
		time.sleep(2)
		driver.find_element_by_xpath("//a[@href='/{}/followers/']".format(willFollow)).click()
		time.sleep(8)

		fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
		scroll = 0
		
		while scroll < 20:	
			driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',fBody)
			time.sleep(0.5)
			scroll += 1
		i = 0
		
		while i < 51:
			takip = driver.find_element_by_xpath("//button[text()= 'Takip Et']")
			takip.click()
			time.sleep(6)
			i += 1
			if i == 51:
				print(datetime.datetime.now())
				time.sleep(900)
				scroll2 = 0
				while scroll2 < 21:	
					driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',fBody)
					time.sleep(0.5)
					scroll2 += 1
					if scroll2 == 21:
						i = 0
					
username = input("Username: ")
password = input("Password: ")
willFollow = input("Whose followers will be followed(Username): ")
print("!!!!!Not: You have to follow the person whose followers will be followed for using this tool.!!!!!")

MyBot = InstagramBot(username, password)
MyBot.login()
MyBot.follow_this_users_followers(willFollow)