a = list(map(float, input("Уведіть 10 значень через пропуск  ").split())) 
s = 0 
for i in a:
    s += i
print ("summa for ", s) 
n=0
b=len(a)
s=0
while n<b:
    s+=a[n]
    n+=1
print ("summa while ", s)
