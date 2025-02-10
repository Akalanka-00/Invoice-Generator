import random

def generate_items_to_purchase(amazon_data, num_items=3):

    selected_products = random.sample(amazon_data, num_items)

    items_to_purchase = {}

    for product in selected_products:
        product_name = product[1]  # Assuming product title is in the first column
        quantity = random.randint(1, 5)
        items_to_purchase[product_name] = quantity

    return items_to_purchase



