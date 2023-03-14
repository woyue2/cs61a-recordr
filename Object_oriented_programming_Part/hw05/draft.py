class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    #######Class Function@classfunc @property used as property
    #Class Attributes
    stock_num = 0
    deposit_moeny = 0
    ##Function
    #Constructors
    def __init__(self,merchandise_name,price):
        self.merchandise_name = merchandise_name
        self.price = price
    #Ways and instance Attributes
    def vend(self):
        if self.stock_num == 0 and self.deposit_moeny == 0:
            return "Machine is out of stock." 
            # return "Machine is out of stock.Here is your $%d" % (self.deposit_moeny)
        else:
            if self.price > self.deposit_moeny:
                return "You must deposit $%d more." % (self.price-self.deposit_moeny)
            else:
                return "Here is your candy and $%d change." % (self.deposit_moeny - self.price)
    def deposit(self,deposit_money):
        self.deposit_money += deposit_money
        return "Current balance: $%d" % (deposit_money)
    def restock(self,stock_num):
        self.stock_num += stock_num
        return "Current candy stock: %d" % (stock_num)