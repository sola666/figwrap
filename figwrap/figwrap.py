import pyfiglet
from colorama import Fore,Back
import os
import tempfile

class figwrap:
    '''
    DESCRIPTION
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        —————————————————————————————————————————————————————————————————————————————————
        A simple class to wrap pyfiglet and colorama to make it easier to render figlet 
        text. This gives the ability to add padding to the left and right of the text and 
        also to give each rendered line a unique colour, for a bit more personalization.
        —————————————————————————————————————————————————————————————————————————————————

    PARAMETERS
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        —————————————————————————————————————————————————————————————————————————————————
        font            : str   ➜  The font to use for the figlet text
        —————————————————————————————————————————————————————————————————————————————————
        renderText      : str   ➜  The text to render
        —————————————————————————————————————————————————————————————————————————————————
        padding_left    : int   ➜  The amount of padding to add to the left of the text
        —————————————————————————————————————————————————————————————————————————————————
        padding_right   : int   ➜  The amount of padding to add to the right of the text
        —————————————————————————————————————————————————————————————————————————————————
    
    ADDITIONAL FEATURES
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        —————————————————————————————————————————————————————————————————————————————————
        method sample_fonts()   ➜  This method will display all available fonts in the
                                    terminal and also write them to a file in the temp
                                    directory. The file will be opened after it has been
                                    written.

    EXAMPLE USAGE
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        —————————————————————————————————————————————————————————————————————————————————
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
    ——————————————————————————————————————————————————————————————————————————————————'''

    def __init__(self,font,renderText,padding_left=0,padding_right=0):
        self.padding_left = padding_left
        self.padding_right = padding_right
        self.fig_lines = [line for line in pyfiglet.Figlet(font=font).renderText(renderText).splitlines()]
        self.__dict__.update({f"line_{i}_colour":Fore.LIGHTWHITE_EX for i,line in enumerate(self.fig_lines)})

    def __call__(self):
        return self.render(render_out=False)
    
    def render(self,render_out=True):
        rendered_text = "\n".join(f"{self.__getattribute__('line_'+str(i)+'_colour')}{' '*self.padding_left if self.padding_left else ''}{f}{' '*self.padding_right if self.padding_right else ''}" for i,f in enumerate(self.fig_lines))
        if render_out:

            print(rendered_text)
        return rendered_text

    def sample_fonts(self):
        import random
        all_Fonts = pyfiglet.FigletFont.getFonts()
        with open(os.path.join(tempfile.gettempdir(),'figwrap_fonts.txt'),'w') as f:
            for font in all_Fonts:
                display_line = f"{font}:\n\n{pyfiglet.Figlet(font=font).renderText('Hello World')}\n{'-'*100}\n"
                f.write(display_line)
                print(f"{random.choice([dict(Fore.__dict__.items())[f] for f in dict(Fore.__dict__.items()).keys()])}{display_line}{Fore.RESET}")
        f.close()
        os.startfile(os.path.join(tempfile.gettempdir(),'figwrap_fonts.txt'))