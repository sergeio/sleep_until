from datetime import datetime
from time import sleep
import sys


def now():
    """Returns the current time in 24-hour format, without leading 0s."""
    return datetime.now().time().isoformat().lstrip('0')

def main(argv):
    """Main loop; checks if it's time to exit every half second."""
    wake_time = argv[1].lstrip('0')
    while not now().startswith(wake_time):
        sleep(.5)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: sleep_until time'
        sys.exit(1)

    main(sys.argv)
