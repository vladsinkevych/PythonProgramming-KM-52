r=int(input("R="))
if r>95 and r<=100:
    print("Excellent")
elif r>=85 and r<95:
    print("Very good")
elif r>=75 and r<85:
    print("Good")
elif r>=65 and r<75:
    print("Satisfactory")
elif r>=60 and r<65:
    print("Marginal")
elif r>=0 and r<60:
    print("Unsatisfactory")
else:
    print("The number given is incorrect, it is negative or greater than 100")