list_items={}
budget=int(input('Enter Your Budget : '))
while True:
    print('Enter 1 to shop')
    print('Enter 2 to Exit')
    choice=int(input('Enter your choice : '))
    if choice==2:
        for k,v in list_items.items():
            if budget==v[1]:
                print('Amount left can buy you '+k)
                break

        print('Grocery list is : ')
        #here  1 tab == 4 spaces
        print('Product name'+'\t'+'Quantity'+'\t'+'Price')
        for k,v in list_items.items():
            print(k,' '*(16-len(k)),v[0],' '*(13-len(str(v[1]))),v[1])
        break
    else:
        product_name=input('Enter Product : ')
        item_quality=input('Enter Quantity : ')
        price=int(input('Enter Price : '))
        if price>budget:
            print('Low Amount please try to buy other products')
        else:
            if product_name in list_items:
                budget+=list_items[product_name][1]
                list_items[product_name]=[item_quality,price]
                budget-=price
            else:
                list_items[product_name]=[item_quality,price]
                budget-=price
                
            print('Amount left',budget)
                
                    
            
