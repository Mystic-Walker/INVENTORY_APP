from datetime import date
import re
class Product:
    'Python OOPs applied'
    def __init__(self, productid = None, productName = None,
                 unitprice = None, categoryid = None,
                 manufacturedate = None,
                 is_active = "Y"):
        self.__product_id = productid
        self.__product_name = productName #validating productname
        self.__unitprice = unitprice
        self.__category_id = categoryid
        self.__manufacture_date = manufacturedate if manufacturedate else date.today()
        self.__is_active = is_active

#---------------------------
#GETTERS AND SETTERS
#---------------------------

    #productid
    def get_product_id(self):
        return self.__product_id
    def set_product_id(self, productid):
        self.__product_id = productid

    def get_productname(self):
        return self.__product_name
    def set_product_name(self, product_name):
        'validate product name before setting'
        pattern = re.compile(r"^[A-Za-z_]{2,30}$")

        while True:
            if pattern.match(product_name):
                self.__product_name = product_name
                break
            else:
                print("\t\t Invalid product name, must have only aplphabets & min 3 characters!!!!....")
                product_name = input("\t\tEnter Product Name again: ")

    #unitprice
    def get_unitprice(self):
        return self.__unitprice
    def set_unitprice(self, unitprice):
        self.__unitprice = unitprice
    
    #categoryid
    def get_category_id(self):
        return self.__category_id
    def set_category_id(self, categoryid):
        self.__category_id = categoryid
    
    #manufacture date
    def get_manufacture_date(self):
        return self.__manufacture_date
    def set_manufacture_date(self, manufacturedate):
        if isinstance(manufacturedate, date):
            self.__manufacture_date = manufacturedate
        else:
            raise ValueError("manufacture date must be date object")
    
    #is active
    def get_is_active(self):
        return self.__is_active
    def set_is_active(self, is_active):
        self.__is_active = is_active

    #override__str__
    def __str__(self):
        return f"""
        productID: {self.__product_id:<10}
        ProductName:{self.__product_name:<10}
        Categoryid: {self.__category_id:<10}
        UnitPrice: {self.__unitprice:<10}
        Manufacture Date: {str(self.__manufacture_date):<10}
        IsActive: {self.__is_active:<10}
        """
    