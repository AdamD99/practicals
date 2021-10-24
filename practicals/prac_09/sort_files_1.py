import shutil
import os


def main():
    os.chdir('FilesToSort/')

    for file in os.listdir('.'):
        sort(file)


def sort(file):
    temp = file.split('.')
    try:
        os.mkdir(temp[1])
    except FileExistsError:
        pass
    shutil.move(file, temp[1] + '/')


main()
