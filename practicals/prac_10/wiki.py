import wikipedia


def main():
    title = input("Enter a Wikipedia page you'd like to explore\n>>> ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        title = input("Enter a Wikipedia page you'd like to explore\n>>> ")


main()
