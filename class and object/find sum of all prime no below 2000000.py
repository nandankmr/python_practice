import math
i = 1
j=0
while i<1000000:
  if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0 and i%23!=0 and i%29!=0:
    k,l=1,0
    while k<math.sqrt(i):
        if i%k==0:
            l+=1
        k+=1
    if l==1:
        j+=i
        print(i)
  i+=1
print(j)

