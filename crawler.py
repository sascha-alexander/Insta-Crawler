#Entering the Instgram Website

import webbrowser

webbrowser.open('https://www.instagram.com/accounts/login/', new=2, autoraise=True)

#Getting the login account data
def get_login():
    user_name = input("Please provide your Instagram account name: ")
    password = input("Please provide your Instagram password: ")


#Locate the username field
unform = browser.find_element_by_name("username")
#Locate the password field
pwform = browser.find_element_by_name('password')

ActionChains(browser)\
    .move_to_element(unform).click()\
    .send_keys('test')\
    .move_to_element(pwform).click()\
    .send_keys('test')\
    .perform()

#Locate login button
login_button = browser.find_element_by_xpath(
'//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')

#Click login button
login_button.click()
