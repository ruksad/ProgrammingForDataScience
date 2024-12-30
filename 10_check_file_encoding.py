from pathlib import Path

import chardet
from timeit_util import time_decorator


@time_decorator
def detect_file_encoding():
    line = '{:<35}{:<10}{}'.format
    print(line('File name', 'Encoding', 'Confidence'))

    for filepath in Path('sources').glob('*'):
        detect = chardet.detect(filepath.read_bytes())  # tells you encoding of the file data and gives the confidence too
        print(line(str(filepath), detect['encoding'], detect['confidence']))


if __name__ == "__main__":
    detect_file_encoding()
