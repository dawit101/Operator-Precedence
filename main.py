#Operator Precedence
#means different operators have precedence over other operators

#the order of precedence is 
#1. ()
#2. **
#3. * or /
#4. + or -


print(20 - 3 * 4) # 3*4=12 then 20-12=8 

print((20 - 10) ** 2) #20-10=10 then 10^2= 100

print(5 * (3.0 + 2.0)) #3.0+2.0=5.0 then 5*5.0=25.0
print(5 * (3 + 2)) #3+2=5 then 5*5=25

x=5
y=2
z=20
m=x**y+z
print(float(m)) #make a equation then float it

x=5
y=2
z=20
m=x**y+z
print(int(m)) #make a equation then int it