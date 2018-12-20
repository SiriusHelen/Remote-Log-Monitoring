
import os.path
import re
from os import path
import apache_log_parser
from pprint import pprint

def second():
    file_path ='C:/xampp/apache/logs/access.log'
    print(file_path)
    with open(file_path) as f:
        new = ' ' + f.read()
        line_parser = apache_log_parser.make_parser("%h %a %v %U %u %f %H %m %X %l %r %p %P %q %R %T ")
        log_line_data = line_parser(new)


def main():
    second()



if __name__ == '__main__':
    main()