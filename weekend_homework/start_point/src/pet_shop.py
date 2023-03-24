# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop,cash):
    shop["admin"]["total_cash"] =  shop["admin"]["total_cash"] + cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, pets_sold):
     shop["admin"]["pets_sold"] =  shop["admin"]["pets_sold"] + pets_sold
    
    
