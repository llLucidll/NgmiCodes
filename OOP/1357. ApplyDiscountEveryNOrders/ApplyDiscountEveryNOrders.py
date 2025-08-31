
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n: int = n
        # Used to keep track of which customer we are on 
        self.current = 0
        self.discount = discount
        # Make a hashmap for easy accessing of price data.
        self.inventory: dict = {x:y for x,y in zip(products, prices)} 
    
    def calcDiscount(self, bill: int) -> int:
        # Check eligibility for discount
        if self.current % self.n == 0:
            return bill * ((100 - self.discount) / 100)
        else:
            return bill
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.current += 1
        if len(product) != len(amount):
            raise ValueError("The product and amount lists are unequal in value")
        
        bill = 0

        for i in range(len(product)):
            price = self.inventory[product[i]]
            bill += price * amount[i]
        
        return self.calcDiscount(bill)