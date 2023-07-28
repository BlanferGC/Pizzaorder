"""""
Author: Blanfer Garcia 

Application Summary: Graphical interface: The application interface displays a welcome message and an image of a pizza.

Pizza size selection: Users can choose between three different pizza sizes: Personal Pan, Medium and Large. Each size comes with an associated price.

Ingredient selection: The application displays a list of available ingredients along with their respective prices. Users can select multiple ingredients to add to their pizza.

Ingredient Display: Each ingredient is represented by an image and is displayed along with its name and price. Users can click on the image of an ingredient to select and deselect it.

Total price update: With each pizza size or ingredient selection, the total price of the order is updated in real time and displayed to the user.

Place the order: Once users have selected the desired pizza size and toppings, they can click on the "Place an order" button to place the order.

Order summary: After placing the order, the application displays a detailed summary with the selected pizza size, the list of toppings and the total price of the order.

Exit the application: To exit the application, users can click on the "Exit" button, which closes the application window.

Summary of the code sections: 
Class PizzaPlanet:
This section defines the main class "PizzaPlanet" which represents the application. It contains the "init" constructor, where the attributes are initialized and the GUI is created. It also contains several methods to handle the application logic, such as updating the price, displaying the ingredients, placing orders and calculating the total price.

def update_price:
This function is a callback that is triggered when the pizza size is changed in the drop-down menu. It updates the total price of the order based on the pizza size selected and the toppings chosen by the user.

def show_ingredients:
This function is a callback that is triggered when the "Add Ingredients" button is clicked. It displays the list of available ingredients along with their images and prices. Users can select or deselect ingredients by clicking on the images.

def get_ingredients_prices:
This function returns a list of ingredient prices in the same order as the list of available ingredients. It is used to calculate the total price of the order.

def reset_order:
This function resets the order details, setting the pizza size, toppings list and total price to their initial values.

def clear_ingredient_images:
This function clears the ingredient images displayed in the GUI. It is used to clear the ingredients frame before displaying a new selection of ingredients.

def add_ingredient:
This function is a callback that is triggered when the image of an ingredient is clicked. It adds or removes the ingredient from the list of selected ingredients and updates the total price accordingly.

def place_order:
This function is a callback that is triggered when the "Place an order" button is clicked. It displays a summary of the order, including the selected pizza size, toppings list, and total price.

def calculate_price:
This function calculates the total price of the order based on the pizza size selected and the toppings chosen by the user.
"""""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class PizzaPlanet:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Planet online ordering")
        self.root.geometry("1250x950")

        # Initialize pizza size and ingredients
        self.size_var = tk.StringVar()

        # List of available ingredients
        self.ingredient_choices = ["Cheese", "Pepperoni", "Ham", "Mushrooms", "Peppers", "Olives"]

        # Prices for each pizza size and ingredients
        self.size_choices = ["Personal Pan", "Medium", "Large"]
        self.size_prices = [5, 7, 10]
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

        # Reset the order
        self.reset_order()

        # Welcome message in the GUI window
        self.label_welcome = ttk.Label(root, text="Welcome to Pizza Planet", font=("Helvetica", 20))
        self.label_welcome.pack(pady=20)

        # Add pizza image
        self.pizza_image = ImageTk.PhotoImage(Image.open('pizza.png').resize((600, 400)))
        self.label_pizza = ttk.Label(root, image=self.pizza_image)
        self.label_pizza.pack()

        # Show the menu for the pizza size
        self.label_size = ttk.Label(root, text="Select the size of the pizza: ")
        self.label_size.pack()
        for size, price in zip(self.size_choices, self.size_prices):
            ttk.Label(root, text=f"{size}: ${price:.2f}").pack()

        self.size_dropdown = ttk.Combobox(root, textvariable=self.size_var, values=self.size_choices)
        self.size_dropdown.pack()

        self.size_dropdown.bind("<<ComboboxSelected>>", lambda event: self.update_price())

        # Create the button to show ingredients
        self.button_show_ingredients = ttk.Button(root, text="Add Ingredients", command=self.show_ingredients)
        self.button_show_ingredients.pack(pady=10)

        # Create a frame to display the ingredient images
        self.ingredient_frame = ttk.Frame(root)
        self.ingredient_frame.pack(pady=10)

        # Create the display for the total price
        self.label_total_price = ttk.Label(root, text="Total Price: $0.00")
        self.label_total_price.pack()

        # Create the button to place the order
        self.button_order = ttk.Button(root, text="Place an order", command=self.place_order)
        self.button_order.pack(pady=20)

        # Create the button to exit the application
        self.button_exit = ttk.Button(root, text="Exit", command=self.root.destroy)
        self.button_exit.pack(pady=10)

        # Load ingredients images
        self.ingredient_images = {
            "Cheese": ImageTk.PhotoImage(Image.open("cheese.png").resize((100, 100))),
            "Pepperoni": ImageTk.PhotoImage(Image.open("pepperoni.png").resize((100, 100))),
            "Ham": ImageTk.PhotoImage(Image.open("ham.png").resize((100, 100))),
            "Mushrooms": ImageTk.PhotoImage(Image.open("mushrooms.png").resize((100, 100))),
            "Peppers": ImageTk.PhotoImage(Image.open("peppers.png").resize((100, 100))),
            "Olives": ImageTk.PhotoImage(Image.open("olives.png").resize((100, 100))),
        }

        # Initialize the ingredient_listbox as None
        self.ingredient_listbox = None

    def update_price(self):
        # Get the selected size and ingredients
        selected_size = self.size_var.get()

        # Check if the ingredient_listbox exists
        if self.ingredient_listbox:
            selected_ingredients = self.ingredient_listbox.curselection()
        else:
            selected_ingredients = []

        # Calculate the total price based on the selected size and ingredients
        size_price = self.prices[selected_size]
        ingredients_price = sum(self.prices[self.ingredient_choices[i]] for i in selected_ingredients)
        total_price = size_price + ingredients_price

        # Update the "Total Price" label with the total price
        self.label_total_price.config(text=f"Total Price: ${total_price:.2f}")

    def show_ingredients(self):
        # Check if the Listbox already exists
        if self.ingredient_listbox:
            self.ingredient_listbox.destroy()

        # Clear the displayed ingredient images
        self.clear_ingredient_images()

        # Show the list of available ingredients with images and prices
        self.label_total_price.config(text="Total Price: $0.00")  # Reset total price display

        # Add Listbox to select ingredients
        self.ingredient_listbox = tk.Listbox(self.ingredient_frame, selectmode=tk.MULTIPLE)
        for ingredient in self.ingredient_choices:
            self.ingredient_listbox.insert(tk.END, ingredient)
        self.ingredient_listbox.pack(side=tk.LEFT)

        # Bind the update_price method to the Listbox selection event
        self.ingredient_listbox.bind("<<ListboxSelect>>", lambda event: self.update_price())

    def get_ingredient_prices(self):
        # Get a list of ingredient prices in the same order as ingredient_choices
        return [self.prices[ingredient] for ingredient in self.ingredient_choices]

    def reset_order(self):
        # Initialize the order details
        self.order = {
            "size": "",
            "ingredients": [],
            "price": 0
        }

    def clear_ingredient_images(self):
        # Clear the displayed ingredient images
        for widget in self.ingredient_frame.winfo_children():
            widget.destroy()

        # Reload ingredient images
        for ingredient in self.ingredient_choices:
            ingredient_label = ttk.Label(self.ingredient_frame, text=f"{ingredient}: ${self.prices[ingredient]:.2f}")
            ingredient_label.pack(side=tk.LEFT)
            image_label = ttk.Label(self.ingredient_frame, image=self.ingredient_images[ingredient])
            image_label.pack(side=tk.LEFT)
            image_label.bind("<Button-1>", lambda event, ing=ingredient: self.add_ingredient(ing))

    def add_ingredient(self, ingredient):
        # Check if the ingredient_listbox exists
        if self.ingredient_listbox:
            selected_ingredients = self.ingredient_listbox.curselection()
        else:
            selected_ingredients = []

        # Get the selected size
        selected_size = self.size_var.get()

        # Calculate the total price based on the selected size and ingredients
        size_price = self.prices[selected_size]
        ingredients_price = sum(self.prices[self.ingredient_choices[i]] for i in selected_ingredients)
        total_price = size_price + ingredients_price

        # Update the "Total Price" label with the total price
        self.label_total_price.config(text=f"Total Price: ${total_price:.2f}")

        # Update the selected ingredients listbox
        if ingredient not in selected_ingredients:
            self.ingredient_listbox.select_set(self.ingredient_choices.index(ingredient))
        else:
            self.ingredient_listbox.selection_clear(self.ingredient_choices.index(ingredient))

    def place_order(self):
        selected_size = self.size_var.get()
        selected_ingredients = self.ingredient_listbox.curselection()

        # Check if the user has selected a size
        if not selected_size:
            messagebox.showerror("Error", "Please select a pizza size.")
            return

        # Check if the user has selected at least one ingredient
        if not selected_ingredients:
            messagebox.showerror("Error", "Please select at least one ingredient")
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
        popup_label.pack(padx=20, pady=20)

        # Reset the order after placing the order
        self.reset_order()

    def calculate_price(self, size, ingredients):
        # Calculate the price based on the pizza size and ingredients
        # Prices are defined in the self.prices dictionary
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