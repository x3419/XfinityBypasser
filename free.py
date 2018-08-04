import random
from splinter import Browser
import uuid
import time
import subprocess
from urllib.request import urlopen

# interface found from 'netsh wlan show interface'

INTERFACE = 'Wi-Fi'

def change_mac():
    process = subprocess.Popen(
        'TMAC.exe -n {} -nr02 -en -s'.format(INTERFACE),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

def connect_to_network():
##
##    process = subprocess.Popen(
##        'netsh wlan add profile filename="xfinity.xml" interface="{}" user=current'.format(INTERFACE),
##        shell=True,
##        stdout=subprocess.PIPE,
##        stderr=subprocess.PIPE)
##    stdout, stderr = process.communicate()
   
    
##    process = subprocess.Popen(
##        'netsh wlan connect xfinitywifi',
##        shell=True,
##        stdout=subprocess.PIPE,
##        stderr=subprocess.PIPE)
##    stdout, stderr = process.communicate()

    subprocess.call(['netsh', 'wlan', 'connect','xfinitywifi'],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
    return 'successfully' in string(stdout)

def free_connect():
    email    = str(random.randrange(10000000,99999999))+'@gmail.com'
    zip_code = random.randrange(10000,99999)
    url      = 'http://www.yahoo.com'

    browser  = Browser()
    browser.driver.minimize_window()
    
    uuid1 = str(uuid.uuid4()).replace('-','')
    uuid2 = str(uuid.uuid4()).replace('-','')
    uuid3 = ''.join([i for i in uuid1 if not i.isdigit()])
    uuid4 = ''.join([i for i in uuid2 if not i.isdigit()])

    browser.visit(url)

    browser.is_element_not_present_by_id('amdocs_signup', wait_time=4)
    browser.find_by_id('amdocs_signup').click()
    browser.is_element_not_present_by_text('Complimentary Hour Pass', wait_time=4)    
    browser.find_by_text('Complimentary Hour Pass').click()
    browser.find_by_id('continueButton').click()
    browser.find_by_id('registerFirstName').fill(uuid3)
    browser.find_by_id('registerLastName').fill(uuid4)
    browser.find_by_id('registerEmail').fill(email)
    browser.find_by_id('registerZipCode').fill(zip_code)
    browser.is_element_not_present_by_id('registerContinueButton', wait_time=3)
    browser.find_by_xpath('//*[@id="registerContinueButton"]').click()
    browser.is_element_not_present_by_id('userName', wait_time=10)
    browser.find_by_id('userName').fill(uuid1)
    browser.find_by_id('password').fill(uuid2[0:12])
    browser.find_by_id('passwordRetype').fill(uuid2[0:12])
    browser.is_element_present_by_xpath('//*[@id="dk0-combobox"]', wait_time=10)
    browser.find_by_xpath('//*[@id="dk0-combobox"]').click()
    browser.find_by_xpath('//*[@id="dk0-What-is your favorite movie?"]').double_click()
    browser.find_by_id('secretAnswer').fill(uuid1[0:5])
    browser.find_by_xpath('//*[@id="submitButton"]').click()

    if 'xwod_ftue.php' in browser.url:
        browser.quit()
        

def isRedirectActive():
    response = urlopen('http://xfinity.com/')
    html = str(response.read())

    if 'WiFi by Comcast' in html:
        return True

def run():
    change_mac()
    
    print('Changed MAC')

    time.sleep(20)


    connected = False
    while not connected:
        try:
            connected = connect_to_network()
        except:
            continue
        
    print('Connected to network')
    
    free_connect()

    print('Wait a few seconds for it to active, and you''re good to go!')


if __name__ == '__main__':

    success = False
    while not success:
        try:
            run()
            success = True
        except:
            print('Failed, trying again...')
            continue









    
