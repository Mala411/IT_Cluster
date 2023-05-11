x=int(input("Введіть число: "))
if not x:
    print("Число 0")
if (x%2 and not x%3 and not x%5 and x%10):
    print ("It is yes", x)
else:
    print("It is no")
    
