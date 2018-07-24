#!-*-coding:utf8-*-
import argparse
import os
from uuid import uuid4
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import contributions.git as git
import contributions.config as config


FONTS = ['arial', 'KeepCalm-Medium']


def argparser():
    epilog = '''Credits Hervé Beraud (4383)'''
    parser = argparse.ArgumentParser(
        description='Generate the most coolest github/gitlab timelines',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=epilog)
    parser.add_argument('text', type=str,
                        help="the text to display")
    parser.add_argument('project', type=str,
                        help="the fake project to commit to")
    parser.add_argument('user', type=str,
                        help="the github/gitlab username to authenticate to")
    parser.add_argument('password', type=str,
                        help="the github/gitlab password to authenticate to")
    parser.add_argument('gitname', type=str,
                        help="the username to commit to")
    parser.add_argument('gitemail', type=str,
                        help="the user email to commit to")
    parser.add_argument('-f', '--font', type=str,
                        choices=[key for key in FONTS],
                        default='KeepCalm-Medium',
                        help="the font to use")
    parser.add_argument('-s', '--space', type=str,
                        default='.',
                        help="the default space character to use")
    parser.add_argument('-p', '--pixel', type=str,
                        default='#',
                        help="the default pixel character to use")
    parser.add_argument('-l', '--left-space', type=int,
                        default=5,
                        help="space at left")
    parser.add_argument('-t', '--top-space', type=int,
                        default=0,
                        help="space at top")
    parser.add_argument('--simulate', action='store_true',
                        default=False,
                        help="simulat display")
    parser.add_argument('--no-push', action='store_true',
                        default=False,
                        help="run without push to repo")
    return parser.parse_args()


def generate_text(text, font, pixel_char, space_char, left_space, top_space):
    image = '/tmp/image.jpg'
    matrice = (0.33, 0.33, 33, 0, 33, 33, 33, 0, 33, 33, 33, 0)
    img = Image.new("RGB", (52, 7), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    print("{}/{}.py".format(config.FONTS_PATH, font))
    font = ImageFont.truetype("{}/{}.py".format(config.FONTS_PATH, font), 8)
    draw.text((left_space, top_space), text, (0, 0, 0), font=font)
    img.convert('RGB').convert('L', matrice).save(image)
    img.save(image)
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    matrix = []
    for line in pixels:
        matrix_line = []
        for el in line:
            if el[0] > 110:
                matrix_line.append(space_char)
            else:
                matrix_line.append(pixel_char)
        matrix.append(matrix_line)
    return matrix


def make_timeline(timeline, pixel, project, github_user, github_pass,
                  gitname, email, no_push):
    identifier = str(uuid4())
    print("Project identifier: {}".format(identifier))
    git.clone(project, identifier)
    os.chdir('/tmp/{}'.format(identifier))
    git.config(gitname, email)
    default_branch = git.create_empty_branch()
    git.brand()
    git.commits(timeline, pixel)
    git.restor_default_branch(default_branch)
    if no_push:
        return
    git.push(github_user, github_pass, project)


def main():
    args = argparser()
    matrix = generate_text(
        args.text,
        args.font,
        args.pixel,
        args.space,
        args.left_space,
        args.top_space)
    for line in matrix:
        print("".join(line))
    if args.simulate:
        return
    make_timeline(matrix, args.pixel, args.project, args.user,
                  args.password, args.gitname, args.gitemail, args.no_push)


if __name__ == "__main__":
    main()
