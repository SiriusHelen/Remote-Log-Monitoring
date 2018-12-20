
import time
import logging
from watchdog.observers import Observer
from watchdog.events import  PatternMatchingEventHandler
from termcolor import colored
import apache_log_parser

class Handler(PatternMatchingEventHandler):
    patterns = [ "*.log"]


    def on_modified(self, event):
        with open(event.src_path, 'r') as log_source:
            log_string = ' ' + log_source.read()
            line_parser = apache_log_parser.make_parser("%h %a %v %U %u %f %H %m %X %l %r %p %P %q %R %T ")
            log_line_data = line_parser(log_string)
            print(log_line_data)


def FileWatch(path):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = path
    observer = Observer()
    observer.schedule(Handler(), path)
    observer.start()


    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



def main():
    FileWatch()



if __name__ == '__main__':
    main()