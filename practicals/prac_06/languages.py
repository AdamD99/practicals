from practicals.prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    dynamic_languages = "The dynamically typed languages are:"
    for language in languages:
        if language.is_dynamic():
            dynamic_languages += "\n{}".format(language.name)
    print(dynamic_languages)


main()
