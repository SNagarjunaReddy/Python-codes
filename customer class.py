class company:
    def name(self,name,Id,order,price):
        self.name=name
        self.Id=Id
        self.order=order
        self.price=price
    def customer_details(self):
        print("name of the customer is", self.name)
        print("Id of the customer is", self.Id)
        print("order placed by the customer is", self.order)
        print("price of the order is", self,price)

