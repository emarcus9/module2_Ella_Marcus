'''
Campus_Cafe.py
-A simple cashier program for campus cafe.
-Displays menu with options and prices.
-Takes input from the user on how many coffees, muffins, and bagels they would like and multiplies it by the costs. 
-Takes input on how much user would like to tip.
-Calculates subtotal, tip, tax, and total.
By: Ella Marcus
Date: 9/19/2025
'''

def menu():
    print("--Campus Cafe--")#will appear as menu
    print("Coffee: $2.25")#will appear as menu
    print("Muffin: $2.75")#will appear as menu
    print("Bagel: $2.50")#will appear as menu

    try:
        q_coffees= int(input("How many coffees would you like? "))#asking for user input about quantity, converting to integer
        q_muffins= int(input("How many muffins would you like? "))#asking for user input about quantity, converting to integer
        q_bagels= int(input("How many bagels would you like? "))#asking for user input about quantity, converting to integer
        q_tip= float(input("Enter tip percent (ex: 10 for 10%): "))#asking for user input about quantity, converting to float

        if q_coffees < 0 or q_muffins < 0 or q_bagels < 0 or q_tip < 0:
            print("Please enter a positive number.")
            return None

    except ValueError:
        print("Please enter a whole number.")
        return None

    return q_coffees, q_muffins, q_bagels, q_tip #return it for later use

#formatting the number output
def format_currency(total):
    return (f"${total:.2f}")#adds a $ and formats the floats to two decimal places

#total cost of items
def line_total(quantity, cost):
    return float(quantity * cost)#multiplies cost of item by quantity

#using a tuple to get amount of tax, tip, and complete total
def compute_totals(subtotal, tax_rate, q_tip):
    tax= tax_rate * subtotal #amount of $tax owed
    tip= q_tip / 100 * subtotal #amount of $tip owed
    total= tax + tip + subtotal #complete total- subtotal + tip + tax
    return tax, tip, total

#will appear as output
def print_receipt(q_coffees, q_muffins, q_bagels, cost_coffees, cost_muffins, cost_bagels, q_tip, subtotal, tax, tip, total):
    print()
    print("--Receipt--")
    print(f"{q_coffees} x Coffee @ $2.25 = {format_currency(cost_coffees)}") #prints what, how many, cost with proper formatting
    print(f"{q_muffins} x Muffin @ $2.75 = {format_currency(cost_muffins)}") #prints what, how many, cost with proper formatting
    print(f"{q_bagels} x Bagel @ $2.50 = {format_currency(cost_bagels)}") #prints what, how many, cost with proper formatting
    print(f" Subtotal: {format_currency(subtotal)}") #subtotal
    print(f" Tax(8.875%): {format_currency(tax)}") #tax
    print(f" Tip ({q_tip}%): {format_currency(tip)}") #tip
    print(f" Total: {format_currency(total)}") #total
    print(f" Thank you for shopping with us!") #thank you!

#main function
def campus_cafe():
    #name first function
    outcome= menu()
    if outcome is None: #so that program stops if an error was entered as input
        return None
    else:
        q_coffees, q_muffins, q_bagels, q_tip= outcome #unpack menu called outcome
        cost_coffees= line_total(q_coffees, 2.25) #total cost of coffees, calling line_total function
        cost_muffins= line_total(q_muffins, 2.75) #total cost of muffins, calling line_total function
        cost_bagels= line_total(q_bagels, 2.50) #total cost of bagels, calling line_total function
        subtotal= cost_coffees + cost_muffins + cost_bagels
        tax, tip, total = compute_totals(subtotal, 0.08875, q_tip) #calling compute_totals function
        print_receipt(q_coffees, q_muffins, q_bagels, cost_coffees, cost_muffins, cost_bagels, q_tip, subtotal, tax, tip, total) #print receipt

if __name__ == "__main__":    
    campus_cafe()




