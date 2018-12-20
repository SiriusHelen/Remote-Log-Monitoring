from filetail import FileTail
import apache_log_parser
import logging, logging.handlers
import time

def LogWatcher(path):
    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.DEBUG)
    socketHandler = logging.handlers.SocketHandler('192.168.168.102',

    rootLogger.addHandler(socketHandler)
    tail = FileTail(path)
    for line in tail:
        line_parser = apache_log_parser.make_parser("%h %a %v %U %u %f %H %m %X %l %r %p %P %q %R %T ")
        log_line_data = line_parser(' ' + line)
        logging.info('%s', log_line_data)


def main():
    try:
        while True:
            LogWatcher()
            time.sleep(5)
    except KeyboardInterrupt:
        print('interrupted')

if __name__ == '__main__':
    main()
