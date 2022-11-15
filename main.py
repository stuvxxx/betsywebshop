__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from peewee import *

def search(term):
    result_list = []
    item_details = []
    query = Product.select()
    for row in query:
        if term.lower() in row.name.lower():
            item_details.append(row.name) 
            result_list.append(item_details)
            item_details = []    
    return result_list

def list_user_products(user_id):
    product_list = []
    user = User.get(User.id == user_id)
    for row in user.products:
        product_list.append(row.name)
    return product_list

def list_products_per_tag(tag_id):
    products_with_tag = []
    query = (Product
             .select()
             .join(TagHanger)
             .join(Tag)
             .where(Tag.name == tag_id))
    for row in query:
        products_with_tag.append(row.name)
    return products_with_tag

def add_product_to_catalog(user_id, product):
    query = Product.get_by_id(product)
    query.owner = user_id
    query.save()
    

def update_stock(product_id, new_quantity):
    query = Product.get_by_id(product_id)
    query.quantity = new_quantity
    query.save()

def remove_product(product_id):
    query = Product.get_by_id(product_id)
    query.delete_instance()      

def purchase_product(product_id, buyer_id, quantity):
    query = Product.get_by_id(product_id)
    query.quantity = query.quantity - quantity
    query.save()
    TransactionDetail.create(
        buyer = buyer_id,
        product = product_id,
        quantity = quantity
    )

        