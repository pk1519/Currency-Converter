import tkinter as tk
from tkinter import ttk, messagebox


class Currency:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def convert_to(self, amount, target_currency):
        return amount * (self.rate / target_currency.rate)


# Update the currency data (dummy exchange rates for today)
currencies = {
    1: Currency("Rupee", 83.0),  # Assume updated exchange rates
    2: Currency("Dollar", 1.0),
    3: Currency("Euro", 1.07),
    4: Currency("Pound", 1.22),
    5: Currency("Yen", 0.0068),
    6: Currency("Yuan", 0.14),
    7: Currency("Australian Dollar", 0.64),
    8: Currency("Canadian Dollar", 0.73),
    9: Currency("Swiss Franc", 1.1),
    10: Currency("Swedish Krona", 0.09),
}


def get_currencies_names():
    return [currency.name for currency in currencies.values()]


def convert_currency():
    try:
        source_index = source_currency_combo.current()
        target_index = target_currency_combo.current()
        amount = float(amount_field.get())

        source_currency = currencies[source_index + 1]
        target_currency = currencies[target_index + 1]

        converted_amount = source_currency.convert_to(amount, target_currency)
        result_label.config(text=f"{amount:.2f} {source_currency.name} = {converted_amount:.2f} {target_currency.name}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("450x250")
root.configure(bg="#F0F8FF")

# Set font styles and colors
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 11)
result_font = ("Arial", 12, "italic")

# Create widgets with upgraded font and color
source_currency_label = ttk.Label(root, text="Source Currency:", font=label_font, background="#F0F8FF")
source_currency_combo = ttk.Combobox(root, values=get_currencies_names(), font=label_font)
source_currency_combo.current(0)

target_currency_label = ttk.Label(root, text="Target Currency:", font=label_font, background="#F0F8FF")
target_currency_combo = ttk.Combobox(root, values=get_currencies_names(), font=label_font)
target_currency_combo.current(1)

amount_label = ttk.Label(root, text="Amount:", font=label_font, background="#F0F8FF")
amount_field = ttk.Entry(root, font=label_font)

convert_button = tk.Button(root, text="Convert", command=convert_currency, bg="#4CAF50", fg="white", font=button_font)
result_label = ttk.Label(root, text="", font=result_font, background="#F0F8FF")

# Layout the widgets using grid layout with some padding
source_currency_label.grid(row=0, column=0, padx=10, pady=10)
source_currency_combo.grid(row=0, column=1, padx=10, pady=10)
target_currency_label.grid(row=1, column=0, padx=10, pady=10)
target_currency_combo.grid(row=1, column=1, padx=10, pady=10)
amount_label.grid(row=2, column=0, padx=10, pady=10)
amount_field.grid(row=2, column=1, padx=10, pady=10)
convert_button.grid(row=3, column=0, padx=10, pady=20, columnspan=2)
result_label.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

# Run the application
root.mainloop()
