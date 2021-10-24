"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os

SPECIAL_CHARACTERS = "()_"


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for i, char in enumerate(filename):
        try:
            if char not in SPECIAL_CHARACTERS and filename[i + 1].isupper():
                new_name += f"{char}_"
            elif char.islower() and (filename[i - 1] == "_" or filename[i - 1] == "("):
                new_name += char.upper()
            else:
                new_name += char
        except IndexError:
            new_name += char
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            new_name = os.path.join(directory_name, new_name)
            filename = os.path.join(directory_name, filename)
            print(new_name)
            os.rename(filename, new_name)


demo_walk()
