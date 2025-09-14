"""
minutes to hours and minutes
converts minutes to hours and minutes
how many minutes: input
minutes//60= hours
remainder% of minutes//60= minutes
print: how many hours and minutes extracted from entry
by: Ella Marcus

"""
    #name of function
def minutes_to_hours_and_minutes():
    minutes = int(input("How many minutes would you like to calculate? ")) #asking user how many minutes, entry minutes by user, converted to integer for math usage
    hours= minutes//60 #entry minutes divided by 60 to get the amount of hours without remainder minutes
    minutes= minutes%60 #entry minutes divided by 60 to find remainder to find how many minutes
    #print on page the amount of hours and minutes calculated
    print("The amount of hours calculated are", hours, "and the amount of remainder minutes calculated are", minutes)

minutes_to_hours_and_minutes()

