score = input("Enter score between 0 to 1: ")

try:
    score = float(score)
    if score < 1:
        if score >= 0.9:
            print('A')
        elif score >= 0.8 and score < 0.9:
            print('B')
        elif score >= 0.7 and score < 0.8:
            print('C')
        elif score >= 0.6 and score < 0.7:
            print('D')
        else:
            print('F')
    else:
        print('Bad Score')
except:
    print("Bad Score")