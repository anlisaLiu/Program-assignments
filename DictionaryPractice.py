values={"teal":"blue","verde":"green","amber":"yellow","lavender":"purple"}
values['teal']
groceries={"chicken":1.49,"beef":1.99,"cheese":2.99,"milk":0.49}
print( "chicken: " + groceeries['chicken'])
print("beef: " + groceries['beef'])
print("cheese: " + groceries['cheese'])
print("milk" + groceries['milk'])

shoes={"jordan13":1,"yeezy":8,"foamposite":10,"airmax":5,"sbdunk":20}
def list_checker ():
    for i in range (0:4):
        if (item1 == groceries[i]):
            item1 = groceries[i]
            else:
                item1= "not found"
            
        if (item2 != groceries[i]):
            item2=groceries[i]
            else:
                item2="not found"

def total_price ("item1","item2"):
    list_checker();
    if(item1 == "not found" or item2=="not found":
        return ("Please input an avaliable value");
        else:
            total-cost= groceries['item1'] + groceries['item2']
            return ("The total price of " + item1 + " and " + item2 + " is " + total-cost + ".");

def price_difference ("item1","item2"):
    list_checker();
    if(item1 == "not found" or item2=="not found":
        return ("Please input an avaliable value");
        else:
            difference = groceries['item1'] - groceries['item2']
            return ("The difference between " + item1 + " and " + item2 + " is " + difference + ".");

def restock("shoe","multiplier"):
    print(shoes)
    addition= shoes[shoe] *multiplier
    shoes.update(shoe:addition)
    print(shoes)
 
def clearence_sale("shoe","clearence"):
    print(shoes)
    sale= shoes[shoe]/clearence
    shoes.update(shoe:clearence)

input ("Please input item1")
input ("please input item2")