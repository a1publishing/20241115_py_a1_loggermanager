import argparse
import datetime
import os
from pathlib import Path

#import sys
#sys.path.insert(0, "H:/dev/_env/py/dev/20241115_logman/logman/src")
import logman 

### functions

# get a formatted date string
def get_yyyymmdd(dt):
  logger2.debug('get_yyyymmdd()')
  return f"{dt.year}{dt.month}{dt.day}"

## logging callback filter function

  # filter only messages with filter string  
def filter_only(record):    
  return filter_str in  record.getMessage()

  # filter out all but debug messages
def filter_debug(record):
  return record.levelname == "DEBUG"

  # filter out messages with filter string  
def filter_out(record):    
  return filter_str not in record.getMessage()


###

# get default logger
logger_manager = logman.get_logger_manager()
logger = logger_manager.get_my_logger('default_console_logger')
logger.info('Created `logger_manager` and `logger`')

# add new logger
my_logger_parms = ({
  'name': 'logger2',
  'handler_names': ('default_streamhandler',)
})
logger_manager.add_my_logger(my_logger_parms)
logger2 = logger_manager.get_my_logger('logger2')
logger2.info('Created `logger2`?')       
logger2.set_level('info')
logger2.info('Created `logger2`!')

# get path command line parameter if supplied
parser = argparse.ArgumentParser()
parser.add_argument('--path', nargs='?', default = os.getcwd())
parser.add_argument('--debug', action="store_true")
try:
    args = parser.parse_args()
except:
    logger.error(f"parser error")
# set logger2 level to debug if req'd
if (args.debug):
    logger2.set_level('debug')
    logger2.info('Set `logger2` level to debug')
# set file path if req'd otherwise use current dir
if (args.path is not None):
    ymd = get_yyyymmdd(datetime.datetime.now())
    filepath = Path(f"{args.path}/logger_{ymd}.log")
    #filepath = Path(filepath)
    logger2.debug(f"filepath: {filepath}")

# add a file handler logger and a combined console and file handler logger
    # set and add a file handler configuration
myh = (
  { 'name': 'default_filehandler',
    'formatter_name': 'default_format',
    'handler_type': 'FileHandler',
    'parms': {
      'filepath': filepath,
      'encoding': "utf-8",
      'mode': "a"
    }
  },
)
logger_manager.add_my_handlers(myh)
    # set and add a couple of logger configurations with the file handler config
myl = (
  { 'name': 'file_logger',
    'level': 'info',
    'handler_names': ('default_filehandler',),
  },
  { 'name': 'console_and_file_logger',
    'level': 'info',
    'handler_names': ('default_streamhandler', 'default_filehandler'),
  }
)
logger_manager.add_my_loggers(myl)

# get the file handler logger and log an entry
file_logger = logger_manager.get_my_logger('file_logger')
file_logger.info('Created `file_logger`')

# get the combined console and file handler logger and log an entry
console_file_logger = logger_manager.get_my_logger('console_and_file_logger')
console_file_logger.info('Created `console_file_logger`')

# add a rotating file handler and a timed rotating file handler
handlers = (
  { 'name': 'rf1',
    'handler_type': 'RotatingFileHandler',
    'parms': {
      'filepath': Path(f"{args.path}/rf_logger_{ymd}.log"),
      'maxBytes': 400,
      'backupCount': 2
    }
  }, 
  { 'name': 'tf1',
    'handler_type': 'TimedRotatingFileHandler',
    'parms': {
      'filepath': Path(f"{args.path}/trf_logger_{ymd}.log"),
      'backupCount': 2,
      #'atTime': datetime.time,
      'backupCount': 2,
      'interval': 30,
      'when': 'S'
    }
  }
)
loggers = (
  { 'name': 'rotating_file_1',
    'handler_names': ('rf1',),
    'level': 'info'
  }, {
    'name': 'timed_rotating_file_1',
    'handler_names': ('tf1',),
    'level': 'info',
})
logger_manager.add_my_handlers(handlers)
logger_manager.add_my_loggers(loggers)

# get the loggers and log entries
rf_logger = logger_manager.get_my_logger('rotating_file_1')
str = 'Created `rotating_file_1`'
rf_logger.info(str)
logger.info(str)
'Created `timed_rotating_file_1`'
rf_logger = logger_manager.get_my_logger('timed_rotating_file_1')
rf_logger.info(str)
logger.info(str)


### accessing logging.logger, eg;

# various filtering examples
  # filter out all but debug messages
logger2.logger.addFilter(filter_debug) 
logger2.logger.debug("debug1")
logger2.logger.info("info1") 
logger2.logger.removeFilter(filter_debug)
logger2.logger.debug("debug2")
logger2.logger.info("info2") 
  # filter only messages with filter string  
global filter_str   # TODO: how to pass filter_str as argument to callback instead.  is it even poss.? 
                    #   (suggestions please to mike@a1publishing.com :)
filter_str = 'foo'
logger2.logger.addFilter(filter_only) 
logger2.logger.info("..foo..")
logger2.logger.info("..bar..")
logger2.logger.info("..blah..")
  # filter out messages with filter string  
logger2.logger.removeFilter(filter_only)
filter_str = 'blah'
logger2.logger.addFilter(filter_out) 
logger2.logger.info("..foo..")
logger2.logger.info("..bar..")
logger2.logger.info("..blah..")
