# Define a class for users
class User:
    # Initialize a user with an id, a username and a credit
    def __init__(self, id, username, credit):
        self.id = id
        self.username = username
        self.credit = credit
        # A user has a list of subscriptions
        self.subscriptions = []
    
    # Add a subscription to the user's list
    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)
    
    # Remove a subscription from the user's list
    def remove_subscription(self, subscription):
        self.subscriptions.remove(subscription)
    
    # Activate a subscription if it is in the user's list
    def activate_subscription(self, subscription):
        if subscription in self.subscriptions:
            subscription.active = True
    
    # Deactivate a subscription if it is in the user's list
    def deactivate_subscription(self, subscription):
        if subscription in self.subscriptions:
            subscription.active = False
    
    # Get the total amount of invoices for the user
    def get_total_invoices(self):
        total = 0
        for sub in self.subscriptions:
            total += len(sub.invoices)
        return total
    
    # Get the total amount of money spent by the user
    def get_total_spent(self):
        spent = 0
        for sub in self.subscriptions:
            for inv in sub.invoices:
                spent += inv.amount
        return spent

# Define a class for subscriptions
class Subscription:
    # Initialize a subscription with a name and a price per 10 minutes
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # A subscription has a list of invoices and an active status 
        self.invoices = []
        self.active = False
    
    # Generate an invoice for the subscription if it is active 
    def generate_invoice(self):
        if self.active:
            start_date = datetime.now()
            end_date = start_date + timedelta(minutes=10)
            amount = self.price 
            invoice = Invoice(start_date, end_date, amount)
            self.invoices.append(invoice)

# Define a class for invoices 
class Invoice:
    # Initialize an invoice with a start date, an end date and an amount 
    def __init__(self, start_date, end_date, amount):
        self.start_date = start_date 
        self.end_date = end_date 
        self.amount = amount 

# Import datetime and timedelta modules to work with dates and times 
from datetime import datetime, timedelta 

# Create some users with different ids, usernames and credits 
user1 = User(1,"Alice",1000) 
user2 = User(2,"Bob",500) 

# Create some subscriptions with different names and prices 
sub1 = Subscription("VM",10) 
sub2 = Subscription("Storage",5) 

# Add some subscriptions to the users' lists 
user1.add_subscription(sub1) 
user1.add_subscription(sub2) 
user2.add_subscription(sub1) 

# Activate some subscriptions for the users  
user1.activate_subscription(sub1)  
user2.activate_subscription(sub1)  

# Generate some invoices for the active subscriptions every 10 minutes (this can be done using a loop or a scheduler)  
sub1.generate_invoice()  
sub2.generate_invoice()  

# Print some statistics for the users  
print(f"{user1.username} has {user1.get_total_invoices()} invoices and has spent {user1.get_total_spent()} dollars.")  
print(f"{user2.username} has {user2.get_total_invoices()} invoices and has spent {user2.get_total_spent()} dollars.")