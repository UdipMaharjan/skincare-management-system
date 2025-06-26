from datetime import datetime

def save_products(product_data):
    try:
        file = open("products.txt", "w")
        for product in product_data.values():
            file.write(", ".join([str(item) for item in product]) + "\n")
        file.close()
        return True
    except:
        print("Error updating products.txt file.")
        return False

def generate_invoice(invoice_id, customer_name, phone_number, items, total_amount, shipping_cost=0):
    try:
        currentTime = datetime.now()
        f = open("sales_invoice_" + invoice_id + ".txt", "w")
        f.write("+" * 80 + "\n")
        f.write("\t\t\tWeCare BEAUTY & SKIN CARE - INVOICE\n")
        f.write("+" * 80 + "\n")
        f.write("Invoice ID: " + invoice_id + "\n")
        f.write("Date: " + str(currentTime.year) + "-" + str(currentTime.month).zfill(2) + "-" + str(currentTime.day).zfill(2) +
                " " + str(currentTime.hour).zfill(2) + ":" + str(currentTime.minute).zfill(2) + ":" + str(currentTime.second).zfill(2) + "\n")
        f.write("Customer: " + customer_name + "\n")
        f.write("Phone: " + phone_number + "\n")
        f.write("+" * 80 + "\n")
        f.write("Product\t\t\t\t\tBrand\t\tQty\tPrice\tTotal\n")
        f.write("+" * 80 + "\n")
        for item in items:
            f.write(item[1] + "\t\t" + item[2] + "\t" + str(item[3]) + "\t" + str(item[5]) + "\t" + str(item[6]) + "\n")
        if any(item[4] > 0 for item in items):
            f.write("\nFree Items:\n")
            for item in items:
                if item[4] > 0:
                    f.write(item[1] + " (" + item[2] + ") - " + str(item[4]) + " free\n")
        f.write("+" * 80 + "\n")
        if shipping_cost > 0:
            f.write("Subtotal: " + str(total_amount - shipping_cost) + "\n")
            f.write("Shipping Cost: " + str(shipping_cost) + "\n")
        f.write("Total Amount: " + str(total_amount) + "\n")
        f.write("+" * 80 + "\n")
        f.write("Thank you for shopping at WeCare!\n")
        f.close()
        return True
    except:
        print("Error writing invoice file.")
        return False

def generate_restock_note(restock_id, vendor_name, items, total_cost):
    try:
        currentTime = datetime.now()
        f = open("restock_note_" + restock_id + ".txt", "w")
        f.write("+" * 80 + "\n")
        f.write("\t\t\tWeCare BEAUTY & SKIN CARE - RESTOCK NOTE\n")
        f.write("+" * 80 + "\n")
        f.write("Restock ID: " + restock_id + "\n")
        f.write("Date: " + str(currentTime.year) + "-" + str(currentTime.month).zfill(2) + "-" + str(currentTime.day).zfill(2) +
                " " + str(currentTime.hour).zfill(2) + ":" + str(currentTime.minute).zfill(2) + ":" + str(currentTime.second).zfill(2) + "\n")
        f.write("Vendor: " + vendor_name + "\n")
        f.write("+" * 80 + "\n")
        f.write("Product\t\tBrand\tQty\tPrice\tTotal\tCountry\n")
        f.write("+" * 80 + "\n")
        for item in items:
            f.write(item[1] + "\t\t" + item[2] + "\t" + str(item[3]) + "\t" + str(item[4]) + "\t" + str(item[5]) + "\t" + item[6] + "\n")
        f.write("+" * 80 + "\n")
        f.write("Total Cost: " + str(total_cost) + "\n")
        f.write("+" * 80 + "\n")
        f.close()
        return True
    except:
        print("Error writing restock note file.")
        return False
