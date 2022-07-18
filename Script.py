
import os
import urllib3
import logging
from random import randint
from argparse import ArgumentParser

from selenium.webdriver.firefox.options import Options
from seleniumwire import webdriver
from time import sleep; 

## logger settings setup

lo = logging.getLogger('rootLogger')
lo.setLevel(logging.INFO)
logFormatter = logging.Formatter(
    '%(levelname)-8s %(asctime)-15s %(process)4d:%(threadName)-11s %(name)s %(message)s')

fileLogging = consoleLogging = True


if fileLogging:
    fileHandler = logging.FileHandler('scraper.log')
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(logging.INFO)
    lo.addHandler(fileHandler)

if consoleLogging:
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.INFO)
    lo.addHandler(consoleHandler)

# urllib network warning disabling
urllib3.disable_warnings()

# utility methods 

def getheaders(headerstring):
    return {ele.split(":")[0].strip(): ":".join(ele.split(":")[1:]).strip() for ele in headers.split("\n")}


def checkcreateos(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        return True
    return False



implicitly_wait = 20; 

def getdirver(headless): 
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=r'./geckodriver',firefox_options=options)
    driver.implicitly_wait(implicitly_wait)
    lo.info("driver created")
    return driver

def getnetworkcalls(driver): 
    rs = []
    for request in driver.requests:
        rs.append(request)
    return rs; 
    



if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument('-u','--url', dest="url" , type=str, help="Enter input filename with extention",required=True)    
    
    parser.add_argument('-e','--endswith', dest="endswith" , type=str, help="Enter last word of the network url",required=True)

    parser.add_argument("--headless", dest="headless", help="increase output verbosity", action="store_true")
    
    args = parser.parse_args();

    lo.info("args : %s" %args)

    driver = getdirver(args.headless)

    driver.get(args.url)
    
    sleep(10); 
    
    rs= getnetworkcalls(driver)
    
    lo.info([ele for ele in rs if ele.url.endswith(args.endswith)])

    driver.close()
    
     
