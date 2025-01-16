import re


def read_date_log(string: str):
    pattern = r'[ \[/:\]]'  # split on everything between [ and ]
    split = re.split(pattern, string)
    print(split)
    print(split[4:11])


def match_timestamp_fromLogs(string: str):
    time_re = r"\[[0-9]{2}/[a-zA-z]{3}/[0-9]{4}:[0-9:\- ]*\]"
    findall = re.findall(time_re, string)  # array  array of strings
    print(findall)

    time_re1 = r"\[([0-9]{2}/[a-zA-z]{3}/[0-9]{4}:[0-9:\- ]*)\]" # split the match into group
    re_findall = re.findall(time_re1, string)
    print(re_findall)

    time_re2 = r"\[([0-9]{2})/([a-zA-z]{3})/([0-9]{4}:[0-9:\- ]*)\]"  # split the match into sub groups
    re_findall_1 = re.findall(time_re2, string)
    print(re_findall_1)


'''
{m, n} Match the preceding character m to n times.
{m} Match the preceding character exactly m times.
{m,} Match the preceding character at least m times.
{,n} Match the preceding character at most n times.
* {0,} zero char or more
. {1,} one char or more 
? {0,1} match preceding char 0 or 1 time only
'''


def match_ssn(string: str):
    pattern = r'\b[0-9]{3,5}-[0-9]{2}-[0-9]{4}\b'
    split = re.findall(pattern, string)
    print(split)


if __name__ == "__main__":
    log = str(
        "169.237.46.168 - - [26/Jan/2004:10:47:58 -0800]\"GET /stat141/Winter04 HTTP/1.1\" 301 328 "
        "\"http://anson.ucdavis.edu/courses\"\"Mozilla/4.0 (compatible; MSIE 6.0;Windows NT 5.0; .NET CLR 1.1.4322)\"")
    read_date_log(log)
    ssn = str("My other number is 5638-13-3842.")
    match_ssn(ssn)
    match_timestamp_fromLogs(log)
