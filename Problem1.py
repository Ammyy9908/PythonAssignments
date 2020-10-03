print("Enter Income")
a=int(input()) 
payable=a+(a*0) if(a<100000) else a+((a-100000)*0.1) if a<500000 else a+(400000*0.1)+((a-500000)*0.2)
print(int(payable))