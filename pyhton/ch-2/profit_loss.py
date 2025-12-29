#if cost price and selling price of an items is input through the keyboard write a program to determine whether the seller has made profit oe incurred loss or no profit no loss. Also determine how much profit he made or loss he incurres.

cost_price = int(input("Enter the cost price"))

selling_price = int(input("Enter the selling price"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("we have made profit of ", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("we have made loss of ", loss)
else:
    print("No profit no loss")