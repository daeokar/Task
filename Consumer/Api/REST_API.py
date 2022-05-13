# Generate trhe API for the order -- order concuming the api 

import requests
import json

class COrder:
    """ Define the class COrder """

    def __init__(self, order_date, product, user):
        self.order_date = order_date
        self.product = product
        self.user = user

def create_order(b):
    """ Function to ccreate the order """

    order = COrder(order_date=b.get("order_date"),
            product=b.get("product"),
            user=b.get("user"),)
    return order

def dict_to_order(data):
    """ Define the function to create the dict of the order """

    l = []
    if type(data) == list:
        for b in data:
            resp = create_order(b)
            l.append(resp)
        return l
    order_obj = create_order(b)
    return order_obj

class RestApi:
    """ Define the Rest Class for order """

    #-- Base urls
    BASE_URL = "http://192.168.0.101:8000/order/"

    #-- Static method utiliti method
    @staticmethod                                       
    def get_single_order(id):
        """ Define fnction to get the single data """

        resp = requests.get(RestApi.BASE_URL + str(id)+ "/")
        # print(resp.status_code)
        # print(resp.content)   
        print(resp.json())                                            #-- python_dict
        return resp

    @staticmethod
    def get_all_order():
        """ Define to get the all data """

        resp = requests.get(RestApi.BASE_URL)
        # print(resp.status_code)                                     #-- 200
        # print(resp.content)                                         #-- data byte string
        print(resp.json())                                            #-- python_dict
        return resp                                                   

    @staticmethod
    def post_order(data):
        """ Define the function to post the data """

        data = {"order_date":data.order_date, "product":data.product, "user":data.user}    
        resp = requests.post(RestApi.BASE_URL, data=data)
        print(resp.content)
        return resp

    @staticmethod 
    def put_order(id):
        """ Define function to update the data """

        data = requests.get(RestApi.BASE_URL + str(id)+ "/")
        resp = requests.put(RestApi.BASE_URL, data=data)
        return resp

    @staticmethod
    def delete_order(id):
        """ Define the function to update the data """
        
        resp = requests.delete(RestApi.BASE_URL + str(id)+ "/")
        return resp

#-- main method
if __name__ == "__main__":
    #-- object creation 
    rest = RestApi()

    #-- get all data
    # resp = rest.get_all_product()
    # print(resp)

    #-- get the single oredr
    # resp = rest.get_single_product(1)
    # print(resp)

    #-- post order
    # data = {'order_date': '2022-05-13T03:48:23.065755Z', 'product': 2}
    # resp = rest.post_order(data)
    # print(resp)

    #-- put order
    # resp = rest.put_order(1)
    # print(resp.status_code)
    # print(resp)

    #-- delete order
    # resp = rest.delete_order(1)
    # print(resp.status_code)
    # print(resp)






