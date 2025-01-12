import re


def read_date_log(string: str):
    pattern = r'[ \[/:\]]'  # split on everything between [ and ]
    split = re.split(pattern, string)
    print(split)
    print(split[4:11])


if __name__ == "__main__":
    log = str(
        "169.237.46.168 - - [26/Jan/2004:10:47:58 -0800]\"GET /stat141/Winter04 HTTP/1.1\" 301 328 "
        "\"http://anson.ucdavis.edu/courses\"\"Mozilla/4.0 (compatible; MSIE 6.0;Windows NT 5.0; .NET CLR 1.1.4322)\"")
    read_date_log(log)
