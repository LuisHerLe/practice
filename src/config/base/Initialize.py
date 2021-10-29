# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:39:36 2021

@author: Lhernandez
"""
import socket
import os, sys
import platform
import logging

class Initialize():
    # =============================================================================
    #  CONSTANTS
    # =============================================================================


    OSTYPE = aux = str(platform.system()).upper() #O.S
    HOSTNAME = socket.gethostname() #System User name
    HOSTIPADDR =  socket.gethostbyname(HOSTNAME) #System IP address
    DATE_FORMAT = "%d/%m/%Y"#Date Format
    ROOT_PATH = os.path.abspath(os.path.join(__file__, '../../../..')) #Root directory
    BASE_PATH_SRC = os.path.abspath(os.path.join(__file__, '../../..')) #BASE DIRECTORY SRC
    JSON_PATH = BASE_PATH_SRC + u'\config\json_locators' #JSON DIRECTORY
    CAPTURES_PATH = BASE_PATH_SRC + "\data\captures" #CAPTURES DIRECTORY
    PATH_FILE_STDOUT = BASE_PATH_SRC + u'\data\stdout' #Path's log
    DEFAULT_BROWSER = 'chrome'
    DEFAULT_FILE_STDOUT = False
    DEFAULT_REPORT_FORMAT = "simple"
    DEFAULT_SLEEP = 1
    DEFAULT_WAIT = 1
    DEFAULT_JSON_NAME = 'smnet_login'
    DEFAULT_OBJECT_FILE = ""
    TESTLINK_API_PYTHON_SERVER_URL='http://192.168.10.20/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
    TESTLINK_API_PYTHON_DEVKEY= '85555d80740def30972e2ed093a00b94'
    DEFAULT_SCREENSHOT_FILE =  {
        "path_file": CAPTURES_PATH,
        "name": "",
        "enableScreenShot": True
        }

    # =============================================================================
    # DEFAULT
    # =============================================================================


    DEFAULT_ENABLE_SCREENSHOT = False
    DEFAULT_DRIVER_MODE = "chrome"
    DEFAULT_ENVIROMENT = 'local'  # 59, dev, uat, default: local
    DEFAULT_URL = 'http:localhost:8080'
    DEFAULT_APPLICATION = '/smnet/'
    DEFAULT_USER_NAME = 'osp'
    DEFAULT_PASSWORD = 'unesmnet12'

    # Validate OS
    if OSTYPE == 'WINDOWS':
        WEBDRIVER_PATH = 'C:\\sm\\apps\\test-tools\\'
        DEFAULT_LOG_PATH = ROOT_PATH + '\\log\\'
    else:
        WEBDRIVER_PATH = '/usr/local/bin/'
        DEFAULT_LOG_PATH = ROOT_PATH + '/log/'

    # =============================================================================
    #  SET UP ENVIROMENT
    # =============================================================================

if __name__ == '__main__':
    # Proyect root directory
    sys.path.append(os.path.abspath(os.path.join(__file__, "../../../..")))

    """ 
    ===========================================================================
    Configure logger, utilities and call main function
    ===========================================================================
    """