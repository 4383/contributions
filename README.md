# Contributions
`/!\ Fresh Paint! Still in development /!\`

Generate personalized github timelines from input text

![Example 4383](https://github.com/4383/contributions/raw/master/assets/images/example-1.png)

## Install
```shell
$ pip install -U contributions
```

## Usage

- First, create a fake [github](https://help.github.com/articles/create-a-repo/) or [gitlab](https://docs.gitlab.com/ee/gitlab-basics/create-project.html) repo
- [Obtain a github personal access token](https://github.com/settings/tokens) or use your password
- Execute the `contribtions` command

Example:
```shell
$ contributions --help
usage: contributions [-h] [-f {arial,KeepCalm-Medium}] [-s SPACE] [-p PIXEL]
                     [-l LEFT_SPACE] [-t TOP_SPACE] [--simulate] [--no-push]
                     text project user password gitname gitemail

Generate the most coolest github/gitlab timelines

positional arguments:
  text                  the text to display
  project               the fake project to commit to
  user                  the github/gitlab username to authenticate to
  password              the github/gitlab password to authenticate to
  gitname               the username to commit to
  gitemail              the user email to commit to

optional arguments:
  -h, --help            show this help message and exit
  -f {arial,KeepCalm-Medium}, --font {arial,KeepCalm-Medium}
                        the font to use
  -s SPACE, --space SPACE
                        the default space character to use
  -p PIXEL, --pixel PIXEL
                        the default pixel character to use
  -l LEFT_SPACE, --left-space LEFT_SPACE
                        space at left
  -t TOP_SPACE, --top-space TOP_SPACE
                        space at top
  --simulate            simulat display
  --no-push             run without push to repo

Credits Hervé Beraud (4383)
$ # /!\ The following command need to be run 4 or 5 times /!\
$ # execute on your project by replacing by yours data
$ contributions \
    BADASS \
    https://github.com/4383/badass \
    <your github/gitlab username> \
    <your github/gitlab token> \
    "Hervé Beraud" \
    herveberaud.pro@gmail.com \
    -l 0
```

## Others examples

![Example Badass](https://github.com/4383/contributions/raw/master/assets/images/example-2.jpeg)
