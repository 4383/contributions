import datetime
import os
from subprocess import Popen, PIPE
import contributions.config as config


def execute(command):
    ok = True
    process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = process.communicate()
    rc = process.returncode
    if rc > 0:
        ok = False
    return ok, output.decode('utf-8'), err.decode('utf-8')


def date(line, column):
    today = datetime.datetime.today()
    current_day = config.WEEKDAY[today.weekday()] + 2
    return today + datetime.timedelta(weeks=-column, days=-current_day)
