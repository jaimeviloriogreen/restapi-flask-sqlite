
class Products:
    @classmethod
    def to_dict(self, result):
        if type(result) == list:    
            products = list( map( lambda product: {"name":product[0], "price":product[1], "qty":product[2]}, result ) )
            return products
        
        product = list(result)
        return {"name":product[0], "price":product[1], "qty":product[2]}
    
    @classmethod
    def validate_keys(self, to_update):
        keys = to_update.keys()
        if "name" in keys and "price" in keys and "qty" in keys:
            return to_update
        return None
        