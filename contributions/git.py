import datetime
import sys
import contributions.utils as utils


def clone(project, identifier):
    cmd = ['git', 'clone', project, '/tmp/{}'.format(identifier)]
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)


def create_empty_branch():
    cmd = ['git', 'checkout', '--orphan', 'contrib-tmp']
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)


def config(username, email):
    cmd = ['git', 'config', '--local', 'user.name', '"{}"'.format(username)]
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)
    cmd = ['git', 'config', '--local', 'user.email', '"{}"'.format(email)]
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)


def brand():
    with open('README.md', 'w+') as readme:
        readme.write("# BADASS\n")
        readme.write("generated at {} with badass-contributions\n".format(
            datetime.datetime.now()))
        readme.write("generated with badass-contributions\n")
    cmd = ['git', 'add', 'README.md']
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)
    cmd = ['git', 'add', 'README.md']
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)
    cmd = ['git', 'commit', '-m', '"log changes"']
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)


def commits(sequence, pixel):
    for line_index, line in enumerate(sequence):
        for column_index, el in enumerate(line):
            if el != pixel:
                continue
            date = utils.date(line_index, column_index)
            cmd = ['git', 'commit', '--allow-empty',
                   '--date="{} +0200"'.format(date.strftime("%c")),
                   '-m', 'commit test']
            for commit in range(50):
                ok, output, err = utils.execute(cmd)
                if not ok:
                    print(err)
                    sys.exit(1)
