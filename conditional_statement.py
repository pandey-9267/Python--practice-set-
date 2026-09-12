# traffic code 

# color = input("color: ")
# if(color == "Red"):
#     print("Stop")
# elif(color == "Yellow"):
#     print("Ready to stop")
# else:
#     print("GO")

# ---------------------------------------------------------

# print output for:--
# A = 5 & G = M
# A = 2 & G = M

A = input("A: ")
G = input("G: ")
if ((A == 1 or A == 2) and G == "M"):
    print("Fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("Fee is 200")
elif(A == 5 and G == "M"):
    print("Fee is 300")
else:
    print("No Fee")
      
