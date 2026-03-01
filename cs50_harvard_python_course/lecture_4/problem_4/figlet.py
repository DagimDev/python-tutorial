import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    
    # Check command-line arguments
    if len(sys.argv) == 1:
        # Zero arguments: random font
        font_name = random.choice(fonts)
    elif len(sys.argv) == 3:
        # Two arguments: check for -f or --font
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        
        font_name = sys.argv[2]
        if font_name not in fonts:
            sys.exit("Invalid usage")
    else:
        # Invalid number of arguments
        sys.exit("Invalid usage")
    
    # Set the font
    figlet.setFont(font=font_name)
    
    # Get text from user
    text = input("Input: ")
    
    # Output text in the desired font
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()