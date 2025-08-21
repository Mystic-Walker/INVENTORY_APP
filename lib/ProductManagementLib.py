from dao.ProductDaoImple import ProductDaoImplementation
from dao.AbstractProductDao import ProductDaoService
from models.product import Product
from datetime import datetime

class ProductManagementLib:
    'handles CRUD logic'
    dao_service:ProductDaoService = ProductDaoImplementation()

    @staticmethod
    def display_all():
        products = ProductManagementLib.dao_service.display_all_products()
        for product in products:
            print(product)
    
    @staticmethod
    def add_product():
        product = Product()
        productname = input("Enter the product Name: ")
        product.set_product_name(productname)
        unitprice = float(input("Enter the Unit Price: "))
        product.set_unitprice(unitprice)
        categoryid = int(input("Enter the Category Id: "))
        product.set_category_id(categoryid)
        m_date = input("Enter manufacture Date(dd/mm/yyyy): ")
        util_date = datetime.strptime(m_date, "%d/%m/%Y")
        conv_m_date = util_date.date()
        product.set_manufacture_date(conv_m_date)

        if ProductManagementLib.dao_service.insert_products(product):
            print("Inserted Successfully!!")
        else:
            print("Something went wrong.....")
        
    @staticmethod
    def update_product():
        searchId = int(input("Enter the product ID: "))
        #create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchId)
        if not product:
            print("Product not found")
            return
        print(product)
        confirm = input("Do you want to edit this data? (y/n)")
        if confirm.lower() == 'y':
            product.set_product_name(input("Enter new product Name: ") or product.get_productname())
            product.set_unitprice(float(input("Enter New Unit Price: ")) or product.get_unitprice())

            #pass the object to dao update
            if ProductManagementLib.dao_service.update_product(product, searchId):
                print("updated successfully ....")
            else:
                print("something went wrong ....")

    @staticmethod
    def search_by_id():
        searchId = int(input("Enter the product ID: "))
        #create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchId)
        if not product:
            print("Product not found")
            return
        print(product)
    
    @staticmethod
    def disable_product():
        searchId = int(input("Enter the product ID: "))
        #create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchId)
        if not product:
            print("Product not found")
            return
        print(product)
        product.set_is_active("N")

        #pass the object to dao update
        if ProductManagementLib.dao_service.disable_product(product, searchId):
            print("updated successfully ....")
        else:
            print("something went wrong ....")

        # if ProductManagementLib.dao_service.disable_product(product, searchId):

    @staticmethod
    def apply_gst_to_product():
        product_id = int(input("Enter the product ID to apply GST: "))
        gst_percent = float(input("Enter GST percentage to apply: "))
        if ProductManagementLib.dao_service.apply_gst(product_id, gst_percent):
            print(f"GST of {gst_percent} applied to product ID (product_id)")
        else:
            print("failed to apply GST")