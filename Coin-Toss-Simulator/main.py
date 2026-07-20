import random

from sqlalchemy import case

print("===========================================")
print("=========== COIN TOSS SIMULATOR ===========")
print("===========================================")

print("1.Toss once ")
print("2.Multiple Times ")
print("3.View Statistics")
print("4.Exit")

print("Choose an option from the menu above: ")

Coin = ["Heads ", "Tails"]

choice =int(input())
#switch case to enter case  acc. to choice 
match choice :
    case 1 :
        #Toss once 
      print("==========================")
      print("Flipping the coin....")
      print ("And the call is " + random.choice(Coin))
        
    case 2 :
      #Toss multiple times 
      print("How much times do you want to toss coin ?")
      toss_times =int(input())
      if(toss_times <= 10):
         print("Wow !" )
      else :
         print("That's a lot of tosses !")
        
      for i in range(1,toss_times+1):
            print("==========================")
            print("Flipping the coin....")
            print ("And the call is " + random.choice(Coin))
           
    case 3:
      #View Statistics
      totals_toss = int(input("Enter the total number of tosses: "))
      heads = int(input("Enter the number of heads: "))
      tails = int(input("Enter the number of tails: "))
      
      head_percentage = float(heads / totals_toss) * 100
      tail_percentage = float(tails / totals_toss) * 100
 

print("Percentage of heads: "+ str(head_percentage)+"%") 
print("Percentage of tails:"+ str(tail_percentage)+"%")

