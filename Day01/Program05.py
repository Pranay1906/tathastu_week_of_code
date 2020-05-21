player01 = int(input("enter run of player 1 "))
player02 = int(input("enter run of player 2 "))
player03 = int(input("enter run of player 3 "))
x = (player01 * 100) / 60
y = (player02 * 100) / 60
z = (player03 * 100) / 60
print("Strike rate of player 1 : ", x)
print("Strike rate of player 2 : ", y)
print("Strike rate of player 3 : ", z)
print("Run when player 1 played 60 balls more: ", player01 * 2)
print("Run when player 2 played 60 balls more :", player02 * 2)
print("Run when player 3 played 60 balls more :", player03 * 2)
print("Maximum no of six player 1 could have hit :", player01 // 6)
print("Maximum no of six player 2 could have hit :", player02 // 6)
print("Maximum no of six player 3 could have hit :", player03 // 6)
