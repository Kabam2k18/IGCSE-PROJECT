lunches =["potato things","noodles","Pho","Hamburger","Sausage","Soup"]
daysw =["Monday","Tuesday","Wednesday","Thursday","Friday","Satuurday","Sunday"]
#print(lunches.append("potato things"))
# Print something in a list: (listname[number of pos])
#print(lunches[1])
days = input("Your meal of your chosen day is ")
for item in range(7):
    if daysw[item] == days:
     print("Your meal of your chosen day is",lunches[item])



