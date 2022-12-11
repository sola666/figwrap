# figwrap

A simple class to wrap pyfiglet and colorama to make it easier to render figlet text. This gives the ability to add padding to the left and right of the text and also to give each rendered line a unique colour, for a bit more personalization.

## Installation

Download the package and import from here, I will be uploading this to pypi as a pip package when I get a moment.

This will become included in the HELIOS lib when I can update the project.

## Usage

```python
# Import figwrap
from figwrap import figwrap

# Instantiate the figwrap class with the font, text to render and padding:
fw = figwrap(font='slant',renderText='Hello World',padding_left=3)

# Change the colour of the second line:
fw.line_1_colour = Fore.RED

# Change the colour of the fourth line:
fw.line_3_colour = Fore.CYAN

# Render the text, either by calling the class or by calling the render method:
print(fw())
fw.render()
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
