from breezypythongui import EasyFrame

class TaxCalc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 280, height = 200, title = "Tax Calculator")

        self.addLabel(text = "Gross income", row = 0, column = 0)
        self.inputField = self.addFloatField(value = 0.0,  row = 0, column = 1, width = 15, precision = 2)

        self.addLabel(text = "Dependents", row = 1, column = 0)
        self.inputfield = self.addIntegerField(value = 0, row = 1, column = 1, width = 8)

        self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2,command = self.compute)

        self.addLabel(text = "Total tax", row = 3, column=0)
        self.outputField = self.addFloatField(value = 0.0, row = 3, column = 1, width = 15, precision = 2, state = "readonly")

    def compute(self):
        try:
            income = self.inputField.getNumber()
            dependents = self.inputfield.getNumber()

            # 2024 standard deduction for single filers and married filing separate
            standard_deduction = 14600

            dependent_deduction = 2000

            total_deductions = standard_deduction + (dependents * dependent_deduction)

            taxable_income = income - total_deductions
            taxable_income = max(taxable_income, 0)

            tax_rate = 0.1
            total_tax = taxable_income * tax_rate

            self.outputField.setNumber(total_tax)

        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")


def main():
    TaxCalc().mainloop()

if __name__ == "__main__":
    main()