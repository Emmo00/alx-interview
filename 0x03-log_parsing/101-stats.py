#!/usr/bin/python3
"""reads stdin line by line and computes metrics
"""


def print_stats(filesize, status_stats):
    """prints stats collected
    """
    print("File size: {}".format(filesize))
    for code in sorted(status_stats):
        if status_stats[code] > 0:
            print("{}: {}".format(code, status_stats[code]))


if __name__ == '__main__':
    import sys
    """main function
    """
    filesize = 0
    status_codes = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }
    i = 1
    try:
        for line in sys.stdin:
            if i % 10 == 0:
                print_stats(filesize, status_codes)
                i = 1
            else:
                i += 1
            data_list = line.split(" ")
            status_in = data_list[-2]
            filesize_in = data_list[-1]
            if int(status_in) in status_codes:
                status_codes[int(status_in)] += 1
            filesize += int(filesize_in)
    except KeyboardInterrupt as ki:
        print_stats(filesize, status_codes)
