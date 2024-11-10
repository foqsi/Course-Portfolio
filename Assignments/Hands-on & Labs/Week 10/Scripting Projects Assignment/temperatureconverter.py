from breezypythongui import EasyFrame

class Temp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=280, height=150, title="Temp Converter")
        self.setResizable(False)

        self.addLabel(text="Fahrenheit", row=0, column=0, sticky="W")
        self.fahrenheit = self.addTextField(text="32", row=1, column=0, width=10, sticky="W")

        self.addLabel(text="Celsius", row=0, column=2, sticky="E")
        self.celsius = self.addTextField(text="0", row=1, column=2, width=10, sticky="E")

        self.addLabel(text="=", row=1, column=1, sticky="NSEW")

        self.addButton(text="Convert", row=2, column=1, columnspan=1, command=self.compute)

        # listeners to clear fields
        self.fahrenheit.bind("<KeyRelease>", self.clearFields)
        self.celsius.bind("<KeyRelease>", self.clearFields)

    def compute(self):
        try:
            fahrenheit_text = self.fahrenheit.getText().strip()
            celsius_text = self.celsius.getText().strip()

            fahrenheit = float(fahrenheit_text) if fahrenheit_text else None
            celsius = float(celsius_text) if celsius_text else None

            if fahrenheit is None and celsius is None:
                self.messageBox(title="Error", message="Please enter a value in either Fahrenheit or Celsius field.")
                return

            if fahrenheit is None:
                fahrenheit = (celsius * 9 / 5) + 32
                self.fahrenheit.setText(str(round(fahrenheit, 2)))
            elif celsius is None:
                celsius = (fahrenheit - 32) * 5 / 9
                self.celsius.setText(str(round(celsius, 2)))

        except ValueError:
            self.messageBox(title="Error", message="Invalid input. Please enter a valid number.")

    def clearFields(self, event):
        if event.widget == self.fahrenheit:
            self.celsius.setText("")
        elif event.widget == self.celsius:
            self.fahrenheit.setText("")

def main():
    Temp().mainloop()

if __name__ == "__main__":
    main()
