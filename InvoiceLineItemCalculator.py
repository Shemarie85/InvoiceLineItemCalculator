#Name : Sheena Watson
#Course Number: CIS216
#Lab: Week 6 Invoice Line Item - Calculator
def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again")

print("The Invoice Line Item Calculator")

while True:
    print("")
    price = get_price()
    quantity = get_quantity()
    total = quantity * price

    print("")
    print(f"PRICE: {price:.2f}")
    print(f"QUANTITY: {quantity}")
    print(f"TOTAL: ${total:.2f}")

    user_input = input("Enter another line item? (y/n): ").lower()
    if user_input != 'y':
        break 
print("Bye!")