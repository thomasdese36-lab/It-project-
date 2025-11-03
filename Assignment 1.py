#               Description:
#   This Python program asks the user to enter their income and 
#   then checks which income range they fall into. Based on that range, 
#   it prints the correct tax percentage. It uses simple if–elif–else conditions 
#   to make sure every income amount gets the right tax rate.

y= input (" Welcome to this page! May I have your name, please? ")
x= int (input (f" {y}, how much is your income in birr ?"))

if x >=0 and x<=2000:
    print ("Your income falls in the 0% tax range.")
    
elif x <=4000:
    print ("Your income falls in the 15% tax range.")
    
elif x<=7000:
    print ("Your income falls in the 20% tax range.")

elif x <=10000:
    print ("Your income falls in the 25% tax range.")
    
elif x <=14000:
    print ("Your income falls in the 30% tax range.")
        
else:
    print ("Your income falls in the 35% tax range.")
    
    
                                          # Done by Thomas A
    
    
    #elif x in range (2001,4000):
    #print ("15%").               how can we use rang instade < or > 
