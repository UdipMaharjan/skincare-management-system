def load_products():
    try:
        file = open("products.txt", "r")
        product_data = {}
        product_index = 1
        data = file.readlines()
        for line in data:
            line = line.replace("\n", "").split(",")
            if len(line) >= 5:
                try:
                    line[2] = int(line[2])
                    line[3] = float(line[3])
                    product_data[product_index] = line
                    product_index += 1
                except ValueError:
                    continue
        file.close()
        return product_data
    except FileNotFoundError:
        print("Error: products.txt file not found!")
        print("Each line should contain: product_name,brand,quantity,price,country")
        print("Example: Vitamin C Serum,Garnier,200,1000,France")
        exit()
