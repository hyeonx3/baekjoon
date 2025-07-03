lst=list(map(int,input().split()))
for i in range(7):
   if abs(lst[i]-lst[i+1])!=1:
      print("mixed")
      quit()
if lst[-1]==1:
   print("descending")
else:
   print("ascending")
   