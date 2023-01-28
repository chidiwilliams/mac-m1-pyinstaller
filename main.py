import logging
import subprocess


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    cmd = subprocess.run(['ffmpeg', '-h'])
    logging.warning('subprocess exited with code %s', cmd.returncode)
    print_hi('PyCharm')
