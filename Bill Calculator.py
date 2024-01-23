def main():

    #Input from user
    original_bill = float(input("Please enter the original bill amount: $"))
    tip_percentage = int(input ("Please enter the tip percentage: "))
   
    #Calculate tax
    tax = original_bill * 0.15

    #Calculate tip
    tip = original_bill * (tip_percentage / 100)

    #Calculate total bill
    total_bill = original_bill + tax + tip
   
    #Output
    print (f"Original bill amount: ${original_bill:.2f}")
    print (f"Tax: ${tax:.2f}")
    print (f"Tip: ${tip:.2f}")
    print (f"Your total bill, including tax and tip, is ${total_bill:.2f}")

if __name__ == "__main__": 
    main()                 