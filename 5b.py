score = input("Enter Score between 0.0 and 1.0:")
score = float(score)
if score<0 or score>1:
    print("error! Score is out of range, Score should be between 0.0 and 1.0")
    exit()
elif score>= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score< 0.6:
    print("F")

