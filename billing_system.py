# SmartBuy Supermarket Billing System

print("WELCOME TO SMARTBUY SUPERMARKET")

another_customer = "yes"

while another_customer.lower() == "yes":

    product_names = []
    quantities = []
    prices = []
    product_totals = []

    total_bill = 0

    more_products = "yes"

    while more_products.lower() == "yes":

        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        product_total = quantity * price

        product_names.append(product_name)
        quantities.append(quantity)
        prices.append(price)
        product_totals.append(product_total)

        total_bill += product_total

        more_products = input("Do you want to add another product? (yes/no): ")

    # Apply discount if bill is above 500
    if total_bill > 500:
        discount = total_bill * 0.10
    else:
        discount = 0

    final_amount = total_bill - discount

    # Print receipt
    print("\n========= RECEIPT =========")

    for i in range(len(product_names)):
        print("Product:", product_names[i])
        print("Quantity:", quantities[i])
        print("Price:", prices[i])
        print("Total:", product_totals[i])
        print("----------------------")

    print("Total Bill: Le", total_bill)
    print("Discount: Le", discount)
    print("Final Amount: Le", final_amount)
    print("==========================")

    another_customer = input("\nProcess another customer? (yes/no): ")

print("Thank you for using SmartBuy Billing System!")