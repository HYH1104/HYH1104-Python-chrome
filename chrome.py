import webbrowser as web
import time
import os
 
web.open_new_tab('https://blog.csdn.net')
time.sleep(1)
os.system('taskkill /im chromedriver.exe /F')
os.system('taskkill /im chrome.exe /F')