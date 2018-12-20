import apache_log_parser

line_parser = apache_log_parser.make_parser("%h %a %v %U %u %f %H %m %X %l %r %p %P %q %R %T ")
log_line_data = line_parser(
    ' 192.168.168.102 - - [02/Feb/2018:00:34:03 +0300] "GET /administrator/index.php HTTP/1.1" 200 5613 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.132 Chrome/63.0.3239.132 Safar')
print(log_line_data)