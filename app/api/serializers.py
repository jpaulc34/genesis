def serialize_category(my_category):
    if not isinstance(my_category, list):
        return {
            "id": str(my_category["id"]),
            "name": my_category["name"],
            "description": my_category["description"]
        }
    return [{
            "id": str(category["id"]),
            "name": category["name"],
            "description": category["description"]
        } for category in my_category]

def serialize_product(my_product):
    if not isinstance(my_product, list):
        return {
            "id":my_product["id"],
            "name":my_product["name"],
            "description": my_product["description"],
            "handle": my_product["handle"],
            "sku": my_product["sku"],
            "quantity": my_product["quantity"],
            "cost_price": my_product["cost_price"],
            "selling_price": my_product["selling_price"]
        }
    return [{
            "id":product["id"],
            "name":product["name"],
            "description": product["description"],
            "handle": product["handle"],
            "sku": product["sku"],
            "quantity": product["quantity"],
            "cost_price": product["cost_price"],
            "selling_price": product["selling_price"]
        } for product in my_product]