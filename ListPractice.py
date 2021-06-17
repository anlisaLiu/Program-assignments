emptyList=[]
cityList=["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cityList)
#                              My New List about water
waterList=["Water Droplets","Rain","Waterfall","Clouds","Drizzle","Ocean","Hurricane","Lake","Sea","Puddles"]
print(waterList)
#                                       appending
emptyList.append("NO ")
emptyList.append("LONGER ")
emptyList.append("EMPTY, ")
emptyList.append("MWAHAHAHA!!!!")
#                       Dont mind me. Hahahahaha.......
print("Is the emptylist empty? (;^;)")
print(emptyList)
#                                        slicing
print(waterList[5:8])
#  changed water droplet to tears and clouds to columbus clouds 
#   and then appended water droplets to list and printed it
waterList[0]="Tears"
waterList[4]="Columbus Clouds"
waterList.pop(9)
waterList.append("Water droplets")
print(waterList)
