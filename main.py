from read import load_products
from write import save_products, generate_invoice, generate_restock_note
from operations import display_products
from datetime import datetime

print("\n")
print("\n")
print("\t \t \t \t \t \t \t \t \t WeCare Wholesale")
print("\n")
print("\t \t \t \t \t \t WeCare Beauty, Kathmandu | Phone No: 9841111111")
print("\n")
print("---")
print("\t \t \t \t \t Welcome to the system! I hope you have a good day ahead!")
print("---")
print("\n")

d = load_products()

main_loop = True
while main_loop:
    print("---")
    print("System below are some of the options for you to carryout the needed operations in the system")
    print("---")
    print("\n")
    print("Press 1 to sale the product to customer.")
    print("Press 2 to purchase from manufacturer.")
    print("Press 3 to Exit from the system.")
    print("\n")
    print("---")
    print("\n")

    try:
        options = int(input("Enter the option to continue: "))
    except ValueError:
        print("Please enter a valid number (1, 2, or 3)")
        continue

    print("\n")

    if options == 1:
        print("---")
        print("For Bill Generation you will have to enter the customer details first: ")
        print("---")
        print("\n")
        name = input("Please enter the name of the Customer: ")
        print("\n")
        phone_number = input("Please enter the phone number of the Customer: ")
        print("\n")

        user_sell_item = []
        spend_total = 0
        sell_loop = True

        while sell_loop:
            display_products(d)

            while True:
                try:
                    product_id = int(input("Please Provide the ID of the product you want to sell: "))
                    if product_id in d:
                        break
                    print("Error: Invalid product ID! Available IDs:", list(d.keys()))
                except ValueError:
                    print("Please enter a valid number for product ID")
            print("\n")

            while True:
                try:
                    product_quantity = int(input("Please Provide the quantity you want to purchase: "))
                    if product_quantity > 0:
                        break
                    print("Quantity must be positive!")
                except ValueError:
                    print("Please enter a valid number for quantity")
            print("\n")

            free_items = product_quantity // 3
            total_quantity = product_quantity + free_items
            current_stock = d[product_id][2]
            if total_quantity > current_stock:
                print("Not enough stock! Available:", current_stock, ", You requested:", total_quantity, "(including", free_items, "free items)")
                continue
            print("\n")

            item_price = d[product_id][3] * 2
            item_total = product_quantity * item_price

            user_sell_item.append([
                product_id,
                d[product_id][0],
                d[product_id][1],
                product_quantity,
                free_items,
                item_price,
                item_total
            ])
            spend_total += item_total
            d[product_id][2] -= total_quantity

            print("\n")
            more = input("Would you like to purchase more items? (yes/no): ").lower()
            if more != 'yes':
                sell_loop = False

        shipping = input("Do you want to ship this order? (yes/no): ").lower()
        shipping_cost = 300 if shipping == 'yes' else 0

        if shipping == 'yes':
            print("Shipping cost: Rs.", shipping_cost)
            spend_total += shipping_cost

        currentTime = datetime.now()
        invoice_id = str(currentTime.year) + str(currentTime.month).zfill(2) + str(currentTime.day).zfill(2) + str(currentTime.hour).zfill(2) + str(currentTime.minute).zfill(2) + str(currentTime.second).zfill(2)
        invoice_saved = generate_invoice(invoice_id, name, phone_number, user_sell_item, spend_total, shipping_cost)
        products_saved = save_products(d)

        print("\n")
        print("+" * 80)
        print("\t\t\tWeCare BEAUTY & SKIN CARE - INVOICE")
        print("+" * 80)
        print("Invoice ID:", invoice_id)
        print("Date:", currentTime.year, "-", str(currentTime.month).zfill(2), "-", str(currentTime.day).zfill(2),
              str(currentTime.hour).zfill(2), ":", str(currentTime.minute).zfill(2), ":", str(currentTime.second).zfill(2))
        print("Customer:", name)
        print("Phone:", phone_number)
        print("+" * 80)
        print("Items Purchased:")
        print("+" * 80)
        for item in user_sell_item:
            print(item[1], "x", item[3], "(+" + str(item[4]) + " free)", "- Rs.", item[5], "each = Rs.", item[6])
        print("+" * 80)
        if shipping == 'yes':
            print("Subtotal: Rs.", spend_total - shipping_cost)
            print("Shipping Cost: Rs.", shipping_cost)
        print("Total Amount: Rs.", spend_total)
        print("+" * 80)
        print("Thank you for your purchase!")
        if invoice_saved:
            print("Invoice saved to sales_invoice_" + invoice_id + ".txt")
        print("\n")

    elif options == 2:
        print("---")
        print("Restocking products from manufacturer")
        print("---")
        print("\n")
        vendor_name = input("Please enter vendor/supplier name: ")
        print("\n")

        restock_items = []
        total_cost = 0
        restock_loop = True

        while restock_loop:
            display_products(d)
            product_type = input("Add new product (n) or restock existing (e)? ")
            print("\n")

            if product_type.lower() == 'e':
                while True:
                    try:
                        product_id = int(input("Enter product ID to restock: "))
                        if product_id in d:
                            break
                        print("Error: Invalid product ID! Available IDs:", list(d.keys()))
                    except ValueError:
                        print("Please enter a valid number for product ID")
                print("\n")

                while True:
                    try:
                        quantity = int(input("Enter quantity to restock: "))
                        if quantity > 0:
                            break
                        print("Quantity must be positive!")
                    except ValueError:
                        print("Please enter a valid number for quantity")
                print("\n")

                update_price = input("Update price? (yes/no): ").lower()
                if update_price == 'yes':
                    while True:
                        try:
                            new_price = float(input("Enter new price: "))
                            if new_price > 0:
                                break
                            print("Price must be positive!")
                        except ValueError:
                            print("Please enter a valid number for price")
                    d[product_id][3] = new_price
                else:
                    new_price = d[product_id][3]
                print("\n")

                item_cost = quantity * new_price
                total_cost += item_cost

                restock_items.append([
                    product_id,
                    d[product_id][0],
                    d[product_id][1],
                    quantity,
                    new_price,
                    item_cost,
                    d[product_id][4]
                ])

                d[product_id][2] += quantity
                print("Updated", d[product_id][0], "stock to", d[product_id][2])

            elif product_type.lower() == 'n':
                product_name = input("Enter product name: ")
                print("\n")
                brand_name = input("Enter brand name: ")
                print("\n")

                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity > 0:
                            break
                        print("Quantity must be positive!")
                    except ValueError:
                        print("Please enter a valid number for quantity")
                print("\n")

                while True:
                    try:
                        price = float(input("Enter price: "))
                        if price > 0:
                            break
                        print("Price must be positive!")
                    except ValueError:
                        print("Please enter a valid number for price")
                print("\n")

                country = input("Enter country of origin: ")
                print("\n")

                item_cost = quantity * price
                total_cost += item_cost
                new_id = max(d.keys()) + 1 if d else 1
                d[new_id] = [product_name, brand_name, quantity, price, country]

                restock_items.append([
                    new_id,
                    product_name,
                    brand_name,
                    quantity,
                    price,
                    item_cost,
                    country
                ])

                print("Added new product:", product_name)

            else:
                print("Invalid option. Please try again.")
                continue

            more = input("Would you like to restock more items? (yes/no): ").lower()
            if more != 'yes':
                restock_loop = False

        if restock_items:
            currentTime = datetime.now()
            restock_id = str(currentTime.year) + str(currentTime.month).zfill(2) + str(currentTime.day).zfill(2) + str(currentTime.hour).zfill(2) + str(currentTime.minute).zfill(2) + str(currentTime.second).zfill(2)
            restock_saved = generate_restock_note(restock_id, vendor_name, restock_items, total_cost)
            products_saved = save_products(d)

            print("\n")
            print("+" * 80)
            print("\t\t\tWeCare BEAUTY & SKIN CARE - RESTOCK NOTE")
            print("+" * 80)
            print("Restock ID:", restock_id)
            print("Date:", currentTime.year, "-", str(currentTime.month).zfill(2), "-", str(currentTime.day).zfill(2),
                  str(currentTime.hour).zfill(2), ":", str(currentTime.minute).zfill(2), ":", str(currentTime.second).zfill(2))
            print("Vendor:", vendor_name)
            print("+" * 80)
            print("Items Restocked:")
            for item in restock_items:
                print(item[1], "x", item[3], "- Rs.", item[4], "each = Rs.", item[5])
            print("+" * 80)
            print("Total Cost: Rs.", total_cost)
            print("+" * 80)
            if restock_saved:
                print("Restock note saved to restock_note_" + restock_id + ".txt")
            print("\n")

    elif options == 3:
        main_loop = False
        print("Thank you for using the system, have a good day!")
        print("\n")

    else:
        print("Your option", options, "does not seem to match our requirement. Please try again.")
        print("\n")
