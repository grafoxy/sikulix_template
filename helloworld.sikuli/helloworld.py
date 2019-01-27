import time
from datetime import datetime
import math
import random
#import requests #ToDo https://answers.launchpad.net/sikuli/+question/222395
import logging; reload(logging)
import platform

startTime = datetime.now()

# Create logger
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger=logging.getLogger('')

# Sets the threshold for this logger to level.
# Logging messages which are less severe than level will be ignored
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
fh = logging.FileHandler('helloworld.log')
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

def example_hover():
    hover("1548539831591.png")
    if bool(exists("1548539894118.png")):
        logger.debug('Hint was found')
        popup('Hint was found')
    else:
        logger.debug('Hint not found')
        popup('Hint not found')
    wait(2)

def example_click():
    try:
        click("1548607847431.png")
# Same as click to coordinates
#       click(Location(24, 700))
        type("Hello World!")
        wait(2)
        type("a",KeyModifier.CTRL)
        type(Key.BACKSPACE)
        wait("1548608061432.png",5)
        type(Key.ESC)
        wait("1548607847431.png",5)
        logger.debug('Search OK')
        popup('Search OK')
    except:
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