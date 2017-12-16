import time


def open_log():
    log_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    log_file = open(log_time, "w", encoding="utf-8")
    return log_file


def print_log(tag, string):
    log = open_log()
    print(tag, string)
    log.write(string)
    log.close()
