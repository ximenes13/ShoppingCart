
cart = {}

def add_to_cart():
    item = input("Enter item name: ").strip()
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid price or quantity.")
        return
    if item in cart:
        cart[item]['quantity'] += quantity
    else:
        cart[item] = {'price': price, 'quantity': quantity}
    print(f"{quantity} x {item} added to cart.")

def remove_from_cart():
    item = input("Enter item name to remove: ").strip()
    if item in cart:
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        print(f"{item} is not in the cart.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("\n--- Shopping Cart ---")
    total = 0
    for item, details in cart.items():
        item_total = details['price'] * details['quantity']
        total += item_total
        print(f"{item} - ${details['price']} x {details['quantity']} = ${item_total:.2f}")
    print(f"Total: ${total:.2f}")

def clear_cart():
    cart.clear()
    print("Cart cleared.")

def menu():
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add to cart")
        print("2. Remove from cart")
        print("3. View cart")
        print("4. Clear cart")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_to_cart()
        elif choice == '2':
            remove_from_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            clear_cart()
        elif choice == '5':
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the menu
menu()
