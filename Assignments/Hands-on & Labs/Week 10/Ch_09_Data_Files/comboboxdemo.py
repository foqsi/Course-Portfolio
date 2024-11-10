from breezypythongui import EasyFrame

class ComboboxDemo(EasyFrame):
    """Tests some combo boxes."""

    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Fruits", row = 0, column = 0)
        self.addLabel(text = "Veggies", row = 0, column = 1)
        self.fruits = self.addCombobox(text = "Apple",
                                       values = ("Banana", "Cherry", "Melon"),
                                       row = 1, column = 0,
                                       command = self.displayFruit)
        self.veggies = self.addCombobox(text = "Carrot",
                                        values = ("Bean", "Celery", "Tater"),
                                        row = 1, column = 1,
                                        command = self.displayVeggie)

    def displayFruit(self):
        """Pops up a message box when the user drops the arrow."""
        fruit = self.fruits.getText()
        self.messageBox(title = "Current Fruit", message = fruit)

    def displayVeggie(self):
        """Pops up a message box when the user drops the arrow."""
        veggie = self.veggies.getText()
        self.messageBox(title = "Current Veggie", message = veggie)

if __name__ == '__main__':
    ComboboxDemo().mainloop()
