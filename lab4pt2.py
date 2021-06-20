#DictionaryPractice.py hase the lab4 instructiond mostly
fruits_color{"apple":"red","banana":"yellow","blueberry":"blue"}

def fruit_color(fruit1,fruit2):
    print("We are mashing fruits today!!!")
    print("let see what colors we get!!! (>-<)")
    if ((fruits_color[fruit1] =="red" and fruit_color[fruit2] =="yellow")or(fruits_color[fruit1] =="yellow" and fruit_color[fruit2] =="red")):
        print("You have made an orange with "+fruit1 +" and "+fruit2+".")
        elif((fruits_color[fruit1] =="red" and fruit_color[fruit2] =="blue")or(fruits_color[fruit1] =="blue" and fruit_color[fruit2] =="red")):
            print("You have made an grape with "+fruit1 +" and "+fruit2+".")
            elif((fruits_color[fruit1] =="yellow" and fruit_color[fruit2] =="blue")or(fruits_color[fruit1] =="blue" and fruit_color[fruit2] =="yellow")):
                print("You have made a cucumber with "+fruit1 +" and "+fruit2+".")
                else:
                    print("Sorry nothing new")
                    print("Please try again")

