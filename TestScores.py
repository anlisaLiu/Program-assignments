testResults=["Bob":(75,65,42,73),"Helen":(62,65,67,79),"Vic":(13,17,19,17)]

def Score(name):
    if name=="Bob":
        print(" Bob's Scores: "+testResults['Bob'])
    if name=="Helen":
        print(" Helen's Scores: "+testResults['Helen'])
    if name=="Vic":
        print(" Vic's Scores: "+testResults['Vic'])