from os import path
import apache_log_parser
from pprint import pprint

def second(s):
    file_path = path.relpath(s)
    with open(file_path) as f:
        new = ' ' + f.read()
        line_parser = apache_log_parser.make_parser("%h %a %v %U %u %f %H %m %X %l %r %p %P %q %R %T ")
        log_line_data = line_parser(new)
        pprint(log_line_data)

def main():
    second()



if __name__ == '__main__':
    main()




