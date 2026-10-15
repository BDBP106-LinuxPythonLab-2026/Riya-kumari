inventory = {
"pen": (10.0, 50), # (price, quantity in stock)
"notebook": (45.0, 20),
"eraser": (5.0, 100),
"marker": (30.0, 15),
}
print(inventory)
entry=""
cart={}

while entry!="done":
    entry=input("Enter your order:<item> <quantity>")
    if entry=="done":
        pass
    else:
        order=entry.split()
        if order[0] in inventory.keys() and order[1].isdigit():
            if int(order[1])<=inventory[order[0]][1]:
                if order[0] in cart.keys():
                    cart[order[0]]=(inventory[order[0]][0],int(order[1])+int(cart[order[0]][1]))
                else:
                    cart[order[0]]=(inventory[order[0]][0],order[1])
                inventory[order[0]]=(inventory[order[0]][0],(inventory[order[0]][1]-int(order[1])))
            else:print("ERROR:insufficient stock")
        else:
            print("ERROR:invalid order")

item=list(cart.keys())
quantity=list(cart.values())
print("item".ljust(10),"Quantity".ljust(10),"Unit_price".ljust(10))
total=0
for i in range(0,len(item)):
    print(item[i].ljust(10),str(quantity[i][1]).ljust(10),str(quantity[i][0]).ljust(10))
    total+=float(quantity[i][1])*quantity[i][0]

print("Total :",total)
if total>500:
    print("Yay! you got a !0% discount!")
    total=total*0.9
    print("Your new total is :",total)

print("Current inventory: ",inventory)

inv=list(inventory.items())
for i in range(0,len(inv)):
    if inv[i][1][1]<10:
        print("LOW STOCK : ",inv[i][0])