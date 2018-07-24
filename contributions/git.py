import datetime
import sys
import textwrap
import contributions.utils as utils


def clone(project, identifier):
    cmd = ['git', 'clone', project, '/tmp/{}'.format(identifier)]
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)


def create_empty_branch():
    cmd = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)
    default_branch = output.replace('\n', '')
    cmd = ['git', 'checkout', '--orphan', 'contrib-tmp']
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)
    return default_branch


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
        readme.write("# Hey you!")
        readme.write(textwrap.dedent("""
            This fake project allow
            [contributions](https://github.com/4383/contributions)
            to generate my personal timeline
            """))
        readme.write(textwrap.dedent("""
            Create your fake repo and get your own :
            ```shell
            $ pip install -U contributions
            $ contributions --help
            ```
            """.format(datetime.datetime.now().strftime("%c"))))
        readme.write(textwrap.dedent(
            """
            Get your
            [BADASS timeline](https://github.com/4383/contributions)\n
            """))
        readme.write("generated at {} with badass-contributions".format(
            datetime.datetime.now().strftime("%c")))
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
            for minute, counter in enumerate(range(10), 5):
                date = utils.date(line_index, column_index, 0, minute)
                cmd = ['git', 'commit', '--allow-empty',
                       '--date="{} +0200"'.format(date.strftime("%c")),
                       '-m', 'badass make commit {}/{}'.format(
                        minute, 0)]
                ok, output, err = utils.execute(cmd)
                if not ok:
                    print(err)
                    sys.exit(1)


def restor_default_branch(branch_name):
    print("Removing original default branch ({})".format(branch_name))
    cmd = ['git', 'branch', '-D', branch_name]
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)
    print("Rename working branch")
    cmd = ['git', 'branch', '-m', branch_name]
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)


def push(username, password, project):
    project = project.replace('https://',
                              'https://{}:{}@'.format(username, password))
    print(project)
    cmd = ['git', 'push', '-f', project]
    ok, output, err = utils.execute(cmd)
    if not ok:
        print(err)
        sys.exit(1)
