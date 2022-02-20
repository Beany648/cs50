f = [1, 100, 1000]
sum=0
for i in f:
    if i == 100 or i == 1:
        #break
        continue
    sum+=i
print(sum)
 