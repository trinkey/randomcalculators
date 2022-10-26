while True:
 m,h=float(input("Total:")),input("Amount:")
 while h!="r":
  print(str(float(h)/m*100)+"%")
  h=input("Amount:")