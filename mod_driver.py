


import cnf_bvb
import emoji
# from pyvirtualdisplay import Display
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
# from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
#from selenium.webdriver import ActionChains
os.system("rm -rf /tmp/*")

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		#os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")

def build_driver(width,height):
	#init_fire()
	print("BUILDING PROFILE DRIVER  ...... ",end='')
	# user_agent = cnf_bvb.user_agent
	
	#random_display_chose=cnf_bvb.random_display_chose
	# width=cnf_bvb.width
	# height=cnf_bvb.height
	#width , height =cnf_bvb.resolution_func()
	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)
	try:
		new_driver_path = cnf_bvb.new_driver_path
		new_binary_path , user_agent = cnf_bvb.random_fir()
		sys_use_agent=re.findall('\(.*?\)',user_agent)[0]
		#print(new_binary_path)
		serv = Service(new_driver_path)
		fp = webdriver.FirefoxProfile()
		ops = Firefox_Options()
		#user_agent = cnf_bvb.user_agent
		#firefox_options = Firefox_Options()		
		ops.add_argument(moz_wid)
		ops.add_argument(moz_hig)
		fp.set_preference('network.proxy.type', 1)
		
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference('useAutomationExtension', False)
		#fp.set_preference("http.response.timeout",95)
		fp.set_preference("dom.popup_maximum", 0)
		fp.set_preference("general.useragent.override",user_agent)
		fp.set_preference('webdriver.load.strategy','unstable')
		fp.set_preference("modifyheaders.headers.count", 2)
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference("modifyheaders.headers.action0", "Add")
		fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		fp.set_preference("dom.push.enabled", False)
		fp.set_preference("intl.accept_languages", "en-GB");
		fp.update_preferences()
		ops.binary_location = new_binary_path
		ops.profile=fp
		#driver = webdriver.Firefox(service=serv, options=ops)
		#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		#driver.set_page_load_timeout(79)

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		#print(new_binary_path)
		print(user_agent)
	except Exception as error:
		print("    Error !!!!! ----->"+str(error))
	return serv ,ops