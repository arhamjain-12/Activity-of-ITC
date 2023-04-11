
"""
The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.
Tariff on Room: Delux Room- 7500 INR
                            Non AC Room- 4500 INR 
You  as a developer has to create a program for a hotel owner which has the following requirements,
The program should begin with taking input from the checkout counter 
Type of room booked 
Total number of days 
Total Amount on Food (Amount is expected )
There are the following cases to be considered while generating a bill.
The tax on food amount is dependent on the type of room booked.
Tax on food for the deluxe room will be billed  18% of the total food amount.
Tax on food for the Non AC room will be billed  5% of the total food amount.
You are supposed to include a tip of 10% on the food amount.
The output from your program should include;
The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 
The tip amount, and the grand total for the meal including both the tax and the tip.
Format the output so that all of the values are displayed using two decimal places.
"""

Room=input("Type of room booked- ")
if Room=="Deluxe Room":
    days=int(input("Total number of days- "))
    food_amount=float(input("Total Amount of food- "))
    Room_Tariff= 7500*days
    tax_on_food=0.18*food_amount
    tip= 0.1*food_amount
    cgst=tax_on_food/2
    sgst=tax_on_food/2
    Total=Room_Tariff+tax_on_food+tip+food_amount
    print("Room Tariff: INR",round(Room_Tariff,2))
    print("Gst- CGST= INR",round(cgst,2),"SGST= INR",round(sgst,2))
    print("Tip: INR",round(tip,2))
    print("Grand Total: INR",round(Total,2))
elif Room=="Non AC Room":
    days=int(input("Total number of days- "))
    food_amount=float(input("Total Amount of food- "))
    Room_Tariff= 4500*days
    tax_on_food=0.05*food_amount
    tip= 0.1*food_amount
    cgst=tax_on_food/2
    sgst=tax_on_food/2
    Total=Room_Tariff+tax_on_food+tip+food_amount
    print("Room Tariff: INR",round(Room_Tariff,2))
    print("Gst- CGST= INR",round(cgst,2),"SGST= INR",round(sgst,2))
    print("Tip: INR",tip)
    print("Grand Total: INR",round(Total,2))
else:
    print("Invalid Room Type")