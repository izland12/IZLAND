
import time
import sys
 
  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib import parse
import random
import pickle


mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

chrome_options.add_argument('headless')


#유동으로하려면 여기 수정 
# nameInput = sys.argv[1]

# pwdInput = sys.argv[2]

subInput = sys.argv[1].replace('test:', '')

encode = parse.unquote_plus(subInput)
 
driver = webdriver.Chrome('C:/python/chromedriver.exe',options=chrome_options) #크롬버젼과 맞는걸로

driver.implicitly_wait(random.randrange(2, 3))

#로그인
# driver.get("https://m.dcinside.com/auth/login?r_url=https%3A%2F%2Fm.dcinside.com%2Faside%3Fr_url%3Dhttps%3A%2F%2Fm.dcinside.com%2Fcategory")

# driver.implicitly_wait(1)

# time.sleep(random.randrange(1, 2))

# driver.find_element_by_name('user_id').send_keys(nameInput)

# driver.implicitly_wait(1)

# time.sleep(random.randrange(1, 2))

# driver.find_element_by_name('user_pw').send_keys(pwdInput)

# driver.implicitly_wait(1)

# time.sleep(random.randrange(1, 2))

# driver.find_element_by_id('login_ok').click()

# driver.implicitly_wait(random.randrange(2, 3))

driver.get("https://m.dcinside.com/board/mnet_k") #갤러리 목록 주소
 
driver.implicitly_wait(5)

cookies = pickle.load(open("C:/Users/Choi minsung/Documents/GitHub/IZLAND/dist/chatIZ/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.implicitly_wait(5)

time.sleep(random.randrange(0, 1))

#글쓰기

driver.get("https://m.dcinside.com/write/mnet_k") #갤러리 글쓰기 주소
 
driver.implicitly_wait(5)
 
#driver.find_element_by_name('name').send_keys(nameInput)#닉네임
 
#driver.implicitly_wait(1)
 
#driver.find_element_by_name('password').send_keys(pwdInput)#비밀번호
 
#driver.implicitly_wait(1)
 
driver.find_element_by_name('subject').send_keys(encode)#제목
 
driver.implicitly_wait(2)

time.sleep(random.randrange(0, 1))
  
driver.find_element_by_id("textBox").send_keys("ㄹㅇㅋㅋ")
 
time.sleep(random.randrange(0, 1))
 
 
 
 
driver.find_element_by_xpath("//button[@type='button'][@class='btn-temp']").click()

time.sleep(1)

driver.quit()