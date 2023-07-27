import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Create an instance with 'init'
class PizzaPlanet:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Planet online ordering")

        # Initialize pizza size and ingredients
        self.size_var = tk.StringVar()
        self.ingredient_var = tk.StringVar()
        self.reset_order()

        # Welcome message in the GUI window
        self.label_welcome = ttk.Label(root, text="Welcome to Pizza Planet", font=("Helvetica", 20))
        self.label_welcome.pack(pady=20)

        # Add pizza image
        self.pizza_image = tk.PhotoImage(file='pizza.png')
        self.label_pizza = ttk.Label(root, image=self.pizza_image)
        self.label_pizza.pack()

        # Show the menu for the pizza size
        self.label_size = ttk.Label(root, text="Select the size of the pizza: ")
        self.label_size.pack()
        self.size_var = tk.StringVar()
        self.size_choices = ["Personal Pan", "Medium", "Large"]
        self.size_dropdown = ttk.Combobox(root, textvariable=self.size_var, values=self.size_choices)
        self.size_dropdown.pack()

        # Show the list of available ingredients
        self.label_ingredients = ttk.Label(root, text="Select the ingredients you want: ")
        self.label_ingredients.pack()
        self.ingredient_choices = ["Cheese", "Pepperoni", "Ham", "Mushrooms", "Peppers", "Olives"]
        self.ingredient_listbox = tk.Listbox(root, listvariable=self.ingredient_var, selectmode="multiple")
        for ingredient in self.ingredient_choices:
            self.ingredient_listbox.insert(tk.END, ingredient)
        self.ingredient_listbox.pack()

        # Create a label to display the ingredients image
        self.ingredient_image_label = ttk.Label(root)
        self.ingredient_image_label.pack()

        # Create the display to the prices
        self.label_price_size = ttk.Label(root, text="Price of Size: ")
        self.label_price_size.pack()
        self.label_price_ingredients = ttk.Label(root, text="Price of ingredients: ")
        self.label_price_ingredients.pack()

        # Create the button to place the order
        self.button_order = ttk.Button(root, text="Place an order", command=self.place_order)
        self.button_order.pack(pady=20)

        # Load ingredients images
        self.ingredient_images = {
            "Cheese": ImageTk.PhotoImage(Image.open("cheese.png")),
            "Pepperoni": ImageTk.PhotoImage(Image.open("pepperoni.png")),
            "Ham": ImageTk.PhotoImage(Image.open("ham.png")),
            "Mushrooms": ImageTk.PhotoImage(Image.open("mushrooms.png")),
            "Peppers": ImageTk.PhotoImage(Image.open("peppers.png")),
            "Olives": ImageTk.PhotoImage(Image.open("olives.png")),
        }

        # Create a dictionary to store prices
        self.prices = {
            "Personal Pan": 5,
            "Medium": 7,
            "Large": 10,
            "Cheese": 1,
            "Pepperoni": 0.5,
            "Ham": 1,
            "Mushrooms": 0.5,
            "Peppers": 0.5,
            "Olives": 0.5,
        }

    def reset_order(self):
        # Initialize the order details
        self.order = {
            "size": "",
            "ingredients": [],
            "price": 0
        }

    def update_ingredient_image(self):

        # Update the ingredient image based on the selected ingredient
        selected_ingredient = self.ingredient_var.get()

        if selected_ingredient in self.ingredient_images:
            self.ingredient_image_label.config(image=self.ingredient_images[selected_ingredient])

        else:
            # If the ingredient is no selected or the image is not available, show default image
            self.ingredient_image_label.config(image=None)

        # Update the price of ingredients
        total_ingredients_price = sum(self.prices[ingredient] for ingredient in self.order["ingredients"])
        self.label_price_ingredients.config(text=f"Price of Ingredients: ${total_ingredients_price:.2f}")

    def place_order(self):
        selected_size = self.size_var.get()
        selected_ingredients = self.ingredient_listbox.curselection()

        # Check if the user has selected a size
        if not selected_size:
            tk.messagebox.showerror("Error", "Please select a pizza size.")
            return

        # Check if the user has selected at least one ingredient
        if not selected_ingredients:
            tk.messagebox.showerror("Error", "Please select at least one ingredient")
            return

        ingredients_list = [self.ingredient_choices[i] for i in selected_ingredients]

        # Calculate the price based on the pizza size and ingredients
        price = self.calculate_price(selected_size, ingredients_list)

        # Update the order details
        self.order["size"] = selected_size
        self.order["ingredients"] = ingredients_list
        self.order["price"] = price

        # Show order summary message
        summary_message = f"Order Summary:\nSize: {self.order['size']}\nIngredients: {', '.join(self.order['ingredients'])}\nPrice: ${self.order['price']}"

        # Show message in a new window
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Order Summary")
        popup_label = ttk.Label(popup_window, text=summary_message, font=("Helvetica", 14))
        popup_label.pack(padx=20, pay=20)

        # Reset the order after placing the order
        self.reset_order()

    #Calculate the price based on the pizza size and ingredients with prices are defined in the self.prices dictionary
    def calculate_price(self, size, ingredients):
        size_price = self.prices[size]
        ingredients_price = sum(self.prices[ingredient] for ingredient in ingredients)
        total_price = size_price + ingredients_price
        return total_price

# create the main window
root = tk.Tk()

# Create an instance of the class
app = PizzaPlanet(root)

# Run the main event
root.mainloop()