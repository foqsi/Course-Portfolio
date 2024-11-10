"""
File: fontdemo.py
Displays the fonts avaliable on your system
and allows you to select and view their look.
"""

from breezypythongui import EasyFrame
from tkinter import font, END

class FontDemo(EasyFrame):
    """Displays the font avaliable on your system
    and allows you to select and view their look."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Font Demo",
                           width = 300, height = 150)

        # Set up the list box
        self.listBox = self.addListbox(row = 1, column = 0,
                                       listItemSelected = self.displayFont)

        # Add font names to the list box and select the first one
        families = list(font.families())
        for fontName in families:
            self.listBox.insert(END, fontName)
        self.listBox.setSelectedIndex(0)

        # Set up the label and its font
        self.fontLabel = self.addLabel(text = families[0],
                                       row = 0, column = 0)
        self.fontLabel["font"] = font.Font(family = families[0],
                                           size = 20)

    # Event handling methods
    def displayFont(self, index):
        """Responds to the selection of font name in the list box.
        Updates the font name and its font in the label."""
        fontName = self.listBox.getSelectedItem()
        self.fontLabel["text"] = fontName
        self.fontLabel["font"] = font.Font(family = fontName, size = 20)
       
def main():
    """Instantiate and pop up the window."""
    FontDemo().mainloop()

# Instantiate and pop up the window."""
if __name__ == "__main__":
    main()
 
