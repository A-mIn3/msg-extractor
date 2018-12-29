import logging
import os
import sys
import traceback

from extract_msg import __doc__, utils
from extract_msg.message import Message

if __name__ == '__main__':
    # Setup logging to stdout, indicate running from cli
    CLI_LOGGING = 'extract_msg_cli'

    args = utils.get_command_args(sys.argv)
    level = logging.INFO if args.verbose else logging.WARNING
    currentdir = os.getcwd() # Store this just in case the paths that have been given are relative
    if args.out_path:
        if not os.path.exists(args.out_path):
            os.makedirs(args.out_path)
        out = args.out_path
    else:
        out = currentdir
    if args.dev:
        import extract_msg.dev
        extract_msg.dev.main(args, sys.argv)
    else:
        utils.setup_logging(args.config_path, level, args.log, args.file_logging)
        for x in args.msgs:
            try:
                with Message(x[0]) as msg:
                    #Right here we should still be in the path in currentdir
                    os.chdir(out)
                    msg.save(toJson = args.json, useFileName = args.use_filename, ContentId = args.cid)
            except Exception as e:
                print("Error with file '" + filename + "': " +
                      traceback.format_exc())
            os.chdir(currentdir)
