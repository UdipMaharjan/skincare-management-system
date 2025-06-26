def display_products(product_data):
    print("*" * 100)
    print("ID \t Name \t\t\t Brand \t\t Quantity \t\t Price \t\t Origin")
    print("*" * 100)
    for key, value in product_data.items():
        print(key, end="\t")
        for item in value:
            print(item, end="\t\t")
        print()
    print("*" * 100)
