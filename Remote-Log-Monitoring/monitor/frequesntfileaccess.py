import logging, logging.handlers
import time
def send_log():
    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.DEBUG)
    socketHandler = logging.handlers.SocketHandler('192.168.168.102',
                    logging.handlers.DEFAULT_TCP_LOGGING_PORT)
# don't bother with a formatter, since a socket handler sends the event as
# an unformatted pickle
    rootLogger.addHandler(socketHandler)

# Now, we can log to the root logger, or any other logger. First the root...
    logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:
    try:
        while True:
            logger1 = logging.getLogger('monitoring')
            logging.basicConfig(format='%(asctime)s %(message)s', filename='monitorresult.log', level=logging.DEBUG)
            logger1.info('file1 accessed by ip 192.168.168.25')
            time.sleep(5)
    except KeyboardInterrupt:
        print('interrupted')






def main():
    try:
        while True:
            send_log()
            time.sleep(5)
    except KeyboardInterrupt:
        print('interrupted')



if __name__ == '__main__':
    main()
