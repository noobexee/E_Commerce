from discountPolicy import *
from customer import Customer
from inventoryManager  import InventoryManager
from product import Product
from cart import *;

def main():
    # Step 1: Create products
    p1 = Product(101, "Keyboard", 1500)
    p2 = Product(102, "Mouse", 800)

    # Step 2: Set inventory
    InventoryManager.set(p1, 10)
    InventoryManager.set(p2, 5)

    # Step 3: Create a customer and assign a cart
    alice = Customer("Alice")
    cart = alice.cart  # Use the customer's cart

    # Step 4: Add items to the cart
    print("\nAdding items to cart...")
    cart.add_item(p1, 2)  # Reserve 2 Keyboards
    cart.add_item(p2, 1)  # Reserve 1 Mouse

    # Step 5: Show cart
    print("\nCart Items:")
    for item in cart.list_items():
        print(f"{item.product.name} x {item.quantity} = {item.total_price()}")

    print(f"Total Price: {cart.total_price()}")

    # Step 6: Remove 1 Keyboard
    print("\nRemoving 1 Keyboard...")
    cart.remove_item(p1, 1)
    print("\nAdd 1 Mouse...")
    cart.add_item(p2, 1)

    # Step 7: Show updated cart
    print("\nUpdated Cart Items:")
    for item in cart.list_items():
        print(f"{item.product.name} x {item.quantity} = {item.total_price()}")

    print(f"Updated Total Price: {cart.total_price()}")

    # Step 8: Simulate placing an order (deduct officially)
    print("\nPlacing order...")
    discount = FixedAmountDiscount(1000)
    alice.place_order(discount_policy=discount)
    order = alice.orders[0];

    # Print order summary
    print("\nOrder summary:")
    for item in order.items:                                    
        print(f"- {item.product.name} x {item.quantity}")                                                      
    print(f"Status: {order.status}")
    print(f"Total (after discount): {order.get_final_amount()}")

if __name__ == "__main__":
    main()