import json
from typing import List, Dict

class Customer:
    def __init__(self, order_id: int, name: str, phone: str, order_items: List[Dict]):
        self.order_id = order_id
        self.name = name
        self.phone = phone
        self.order_items = order_items



MENU_FILE = "menu.json"
ORDER_FILE = "order.json"

with open(MENU_FILE, "r") as file:
    menu_items = json.load(file)

def menu():
    
    print("\nHere are the available menu items:")
    print("--------------------------------------------------")
    col1 = menu_items[:15]
    col2 = menu_items[15:]
    while len(col2) < len(col1):
        col2.append({"id": "", "name": "", "price": 0.0})

    for left, right in zip(col1, col2):
        left_str = f"{left['id']}. {left['name']} - Rs.{left['price']:.2f}"
        right_str = f"{right['id']}. {right['name']} - Rs.{right['price']:.2f}" if right["id"] != "" else ""
        print(f"{left_str:<40} {right_str}")
    print("--------------------------------------------------\n")
    
    
def order_food():
    print("\n<---Order Food--->\n")
    order_id = 1  
    cust_name = input("Enter your name: ")
    cust_phone = input("Enter your phone number: ")
    
    order_items = []
    while True:
        try:
            item_id = int(input("Enter the item ID to order (or 0 to finish): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if item_id == 0:
            break

        try:
            item_quantity = int(input("Enter the number of items you want to order: "))
            if item_quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid quantity.")
            continue
        
        for item in menu_items:
            if item["id"] == item_id:
                order_items.append({"id": item_id, "quantity": item_quantity, "name": item["name"], "price": item["price"]})
        

    if order_items:
        orders = []
        customer = Customer(order_id, cust_name, cust_phone, order_items)
        print("\nOrder Placed Successfully!\n")
        print("Customer Name:", customer.name)
        print("Phone:", customer.phone)
        print("Ordered Items:\n")
        for item in customer.order_items:
            print(f"  Item ID: {item['id']} | Quantity: {item['quantity']} | Name: {item['name']} | Price: Rs.{item['price']:.2f} x {item['quantity']}")
        subtotal = sum(item['price'] * item['quantity'] for item in customer.order_items)
        print(f"\nTotal Price: Rs.{subtotal:.2f}\n")
        orders.append(customer.__dict__)
        with open(ORDER_FILE, "w") as file:
            json.dump(orders, file, indent=2)
        
    else:
        print("No items ordered.")


def main():
    print("\n<---Welcome to Our Restaurant Service Platform--->\n")
    options = ["See Menu", "Order Food", "Exit"]
    condition = True
    while condition:
        for index, option in enumerate(options):
            print(f"{index+1}. {option}")
            
        user_input = input("\nSelect: ")
        
        if user_input == "1":
            menu()
        
        elif user_input == "2":
            order_food()
        
        elif user_input == "3":
            print("\n---Good Bye---")
            condition = False
            
        else:
            print("Invalid Input! try again")
            
if __name__ == "__main__":
    main()