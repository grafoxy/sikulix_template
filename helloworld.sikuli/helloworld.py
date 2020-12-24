import time
from datetime import datetime
import math
import random
#import requests #ToDo https://answers.launchpad.net/sikuli/+question/222395
import logging; reload(logging)
import platform
import shutil
import glob
import os
import platform
from guide import *

import fake

# Clean up tmp folder
tmpDir = os.path.join(os.getcwd(), 'tmp');
files = glob.glob(os.path.join(tmpDir,'*'))
for f in files:
    os.remove(f)

# For take screenshot on error used some_region:
# SCREEN # for whole screen
# App.focusedWindow() # for the frontmost window
some_region = SCREEN

# switchApp("Chrome");

startTime = datetime.now()

# Create logger
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger=logging.getLogger('')

# Sets the threshold for this logger to level.
# Logging messages which are less severe than level will be ignored
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
fh = logging.FileHandler(os.path.join(tmpDir, 'logs.log'))
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
fh.setFormatter(formatter)
logger.addHandler(fh)

# Configure hotkey "Ctrl+Alt+Space" for stop script
def off (event):
    logger.warning('### Script stopped by hotkey ###')
    duration = datetime.now() - startTime
    logger.warning('### Duration: '+str(duration)+' ###')
    popup('The program is completed.\n Duration'+str(duration)+'\nDone...\nGood Luck')
    exit()

Env.addHotkey(Key.SPACE, KeyModifier.ALT+KeyModifier.CTRL, off)

# Logging initial data
logger.warning('### Initialization script ###')
logger.warning('System: '+platform.system()+' '+platform.release())
logger.warning('Python version: '+platform.python_version())

# Test different log levels
logger.debug('log level DEBUG')
logger.info('log level INFO')
logger.warning('log level WARNING')
logger.error('log level ERROR')
logger.critical('log level CRITICAL')

#Control the time taken for mouse movement to a target location. Default 0.5 second
#Setting it to 0 will switch off any animation
Settings.MoveMouseDelay = 0.5

notificaitonCenterIcon = "1608837173948.png";
notificationsHint = "1608837210755.png";
startButton = "1608837110616.png";
searchIcon = "1548608061432.png";
searchIconBig="1608839000768.png";


def example_hover():
    hover(notificaitonCenterIcon)
    if bool(exists(notificationsHint)):
        logger.debug('Hint was found')
        popup('Hint was found')
    else:
        logger.debug('Hint not found')
        popup('Hint not found')
    wait(2)

def example_click():
    try:
        text(startButton, "This is start button")
        show(3)
        click(startButton)
        # Same as click to coordinates
        #click(Location(24, 700))
        type("Hello World!")

        wait(searchIconBig,5)
        rectangle(searchIconBig)
        show(3)

        type("a",KeyModifier.CTRL)
        type(Key.BACKSPACE)
        wait(searchIcon,5)
        type(Key.ESC)
        wait(startButton,5)
        logger.debug('Search "Hello World!": Done')

        randomName = str(fake.name())
        click(startButton)
        type(randomName)
        wait(5)
        type("a",KeyModifier.CTRL)
        type(Key.BACKSPACE)
        wait(searchIcon,5)
        type(Key.ESC)
        wait(startButton,5)
        logger.debug('Search '+randomName+': Done')
        popup('Search "'+randomName+'": Done.\n Duration: '+str(datetime.now() - startTime)+'\n')

        #Make screeenshot to log dir
        img = capture(some_region)
        print("Saved screen as "+str(img))
        shutil.move(img, os.path.join(tmpDir, 'screenshot_'+str(n)+'.png'))
    except:
    #except Exception as e:
        #logger.error('Exception '+str(e))
        logger.debug('Search FAILED')
        popup('Search FAILED')
   

# Main
example_hover()
example_click()

# Loop and loop control (break, continue and pass)
n = 5
while n > 0:
    if n == 4:
        logger.debug('Cycle n=4')
    if n == 3:
        pass
        logger.debug('Cycle n=3')
    if n == 2:
        n = n - 1
        continue
        logger.debug('Cycle n=2')
    if n == 1:
        break
        logger.debug('Cycle n=1')
    n = n - 1

# Close script
duration = datetime.now() - startTime
logger.warning('### Duration: '+str(duration)+' ###')