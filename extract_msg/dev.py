"""
Module for collecting data to be sent to the developer.
"""

# NOTE: Order of tasks:
#    1. Check for exceptions:
#        * Check the entire process for exceptions raised by a specific file and log them. If none occur, log something like "No exceptions were detected."
#    2. Run the file through the developer versions of the classes


import logging

from extract_msg import dev_classes
from extract_msg import utils



logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def setup_dev_logger(default_path=None, logfile = None, env_key='EXTRACT_MSG_LOG_CFG'):
    utils.setup_logging(default_path, 5, logfile, True, env_key)




def main(args, argv):
    """
    Please only run this from the command line. Attempting to use this
    otherwise is likely to fail. :param args: is the class instance
    returned by `extract_msg.utils.get_command_args`. :param argv: is
    the list of arguments that were the input to the aforementioned
    function.
    """
    setup_dev_logger(args.config_path, args.log)
    for y, x in enumerate(args.msgs):
        logger.log(5, 'RUNNING DEVELOPER MODE ON FILE {}'.format(x[0]))
        try:
            with Message(x[0]) as msg:
                #Right here we should still be in the path in currentdir
                os.chdir(out)
                msg.save(toJson = args.json, useFileName = args.use_filename, ContentId = args.cid)
        except Exception as e:
            logger.exception(e)
        os.chdir(currentdir)
