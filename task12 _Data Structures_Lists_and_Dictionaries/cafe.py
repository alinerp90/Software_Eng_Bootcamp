"""
Imagine you are running a cafe. 
1. Create a list called menu, which should contain at least four items sold in the cafe.
2. Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
3. Create another dictionary called price, which should contain the prices for each item on your menu.
4. Next, calculate the total_stock worth in the cafe. You will need to remember to loop through the appropriate dictionaries and lists to do this.
Tip: When you loop through the menu list, the ‘items’ can be set as keys to access the corresponding ‘stock’ and ‘price’ values. Each ‘item_value’ is calculated by multiplying the stock value by the price value. For example:
item_value = (stock[items] * price[items])
5. Finally, print out the result of your calculation.
"""

menu = ['espresso', 'sandwich', 'juice', 'cake'] #item for sell in the coffee
stock = {'espresso' : 2, 'sandwich' : 5, 'juice' : 3, 'cake' : 7} #stock number of each item
price = {'espresso' : 3 , 'sandwich' : 5 , 'juice' : 6, 'cake' : 4 } #value of each item for sell

stock_value = {} 
total_stock = 0

for item in menu: #populate stock_value{} with a key from menu and value following the calculation stock[item] * price[item]  
    item_value = stock[item] * price[item]
    stock_value[item] = item_value #stock_value[key] = value
    total_stock += item_value #calculate the total value of stock

print(stock_value)
print("The total value of the stock is:" , total_stock)

