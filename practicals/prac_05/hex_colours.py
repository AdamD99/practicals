
HEX_COLOURS = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "burlywood": "#deb887", "chartreuse1": "#7fff00", "chocolate": "#d2691e", "CornflowerBlue": "#6495ed", "DarkGoldenrod": "#b8860b", "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc", "DarkViolet": "#9400d3"}

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
