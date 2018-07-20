import datetime
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


def date(line, column, hour, minute):
    today = datetime.datetime.today()
    today = datetime.datetime(today.year, today.month, today.day, hour, minute)
    current_week_day_to_remove = config.WEEKDAY[today.weekday()] - line
    column = 52 - column
    return today + datetime.timedelta(weeks=-column,
                                      days=-current_week_day_to_remove)
