from sqlite3 import Error

class ModelProducts:
    @classmethod
    def all_products(self, conn):
        sql = "SELECT name, price, qty FROM products"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as err:
            print(f"Error: {err}")
        finally:
            if conn is not None:
                conn.close()
        
        return conn
    
    @classmethod
    def one_product(self, conn, name):
        sql = "SELECT name, price, qty FROM products WHERE LOWER(name) = ?"
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (name.lower(),))
            rows = cursor.fetchone()
            return rows
        except Error as err:
            print(f"Error: {err}")
        finally:
            if conn is not None:
                conn.close()
        
        return conn
    
    @classmethod
    def delete_product(self, conn, name):
        sql = "DELETE FROM products WHERE LOWER(name) = ?"
        name = name.lower()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (name,))
            conn.commit()
            row_delete = cursor.rowcount
            return row_delete
        except Error as err:
            print(f"Error: {err}")
        finally:
            if conn is not None:
                conn.close()
        
        return conn
    
    @classmethod
    def update_product(self, conn, product):
        sql = "UPDATE products SET price = ?, qty = ? WHERE LOWER(name) = ?"
       
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (product['price'], product['qty'], product['name'].lower()  ))
            conn.commit()
            row_update = cursor.rowcount
            return row_update
        except Error as err:
            print(f"Error: {err}")
        finally:
            if conn is not None:
                conn.close()
        
        return conn
       
    @classmethod
    def insert_product(self, conn, product):
        sql = "INSERT INTO products(name, price, qty) VALUES(?, ?, ?)"
       
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (product['name'], product['price'], product['qty'], ))
            conn.commit()
            row_update = cursor.rowcount
            return row_update
        except Error as err:
            print(f"Error: {err}")
        finally:
            if conn is not None:
                conn.close()
        
        return conn