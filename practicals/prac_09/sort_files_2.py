import shutil
import os


def main():
    os.chdir('FilesToSort/')
    categories = {}

    for file in os.listdir('.'):
        temp = file.split('.')
        extension = temp[1]

        if extension not in categories:
            directory = input(f"What category would you like to sort {extension} files into? ")
            categories[extension] = directory
            try:
                os.mkdir(directory)
            except FileExistsError:
                pass
        shutil.move(file, categories[extension] + '/')


main()
