def money():
    Amount_Due = 50
    total_inserted = 0
    
    while total_inserted < Amount_Due:
        Insert_Coin = int(input("Insert Coin: "))
        
        if Insert_Coin in [5, 10, 25]:
            total_inserted += Insert_Coin
            remaining_amount = Amount_Due - total_inserted
            print("Amount Due:", remaining_amount)
        else:
            print("Amount Due:", Amount_Due)
    
    if total_inserted > Amount_Due:
        change = total_inserted - Amount_Due
        print("Change owed:", change)
    elif total_inserted == Amount_Due:
        print("Change Owed: 0")

money()
