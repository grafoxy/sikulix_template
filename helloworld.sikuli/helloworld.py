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
    hover("1548539831591.png");
    if bool(exists("1548539894118.png")):
        logger.debug('Hint was found')
        popup('Hint was found')
    else:
        logger.debug('log level DEBUG')
        popup('Hint not found')
    wait(2);

# Main
example_hover()

# Close script
duration = datetime.now() - startTime
logger.warning('### Duration: '+str(duration)+' ###')