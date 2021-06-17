#===========================================================
#
#  Title:       Big Shreks Appliance.py
#  Course:      CPS 120 Section 03
#  Homework:    Three
#  Author:      Lauren Acton
#  Date:        February 16, 2021
#  Description:
#       < Calculated cost and profit based on input of appliance choice >
#
#===========================================================

print("Big Shrek's Appliance\n")

#Input
Appliance = input("Enter the appliance: ")
WholesaleCost = float(input("Enter Wholesale Cost ($) : "))
RetailPrice = float(input ("Enter Retail Price ($) : "))


#Processing
Profit =(RetailPrice-WholesaleCost)
SalesCommission =(Profit*0.02)
SalesTax =(RetailPrice*0.06)
TotalCost =(RetailPrice+SalesTax)

#Output
if(Appliance == "washer" or Appliance == "Washer"):
    print(f"Appliance Purchased: {Appliance:>9s}")
    print(f"Wholesale Cost:   ${WholesaleCost:10.2f}")
    print(f"Retail Price:     ${RetailPrice:10.2f}\n")
    print(f"Store Profit:     ${Profit:10.2f}")
    print(f"Sales Commission: ${SalesCommission:10.2f}")
    print(f"Sales Tax:        ${SalesTax:10.2f}")
    print(f"Customer Price:   ${TotalCost:10.2f}")
if(Appliance == "dryer" or Appliance == "Dryer"):
    print(f"Appliance Purchased: {Appliance:>9s}")
    print(f"Wholesale Cost:   ${WholesaleCost:10.2f}")
    print(f"Retail Price:     ${RetailPrice:10.2f}\n")
    print(f"Store Profit:     ${Profit:10.2f}")
    print(f"Sales Commission: ${SalesCommission:10.2f}")
    print(f"Sales Tax:        ${SalesTax:10.2f}")
    print(f"Customer Price:   ${TotalCost:10.2f}")
if(Appliance == "refrigerator" or Appliance == "Refrigerator" or Appliance == "frig" or Appliance == "Frig"):
    print(f"Appliance Purchased: {Appliance:>7s}")
    print(f"Wholesale Cost:  ${WholesaleCost:10.2f}")
    print(f"Retail Price:    ${RetailPrice:10.2f}\n")
    print(f"Store Profit:    ${Profit:10.2f}")
    print(f"Sales Commission:${SalesCommission:10.2f}")
    print(f"Sales Tax:       ${SalesTax:10.2f}")
    print(f"Customer Price:  ${TotalCost:10.2f}")
if(Appliance == "microwave" or Appliance == "Microwave"):
    print(f"Appliance Purchased: {Appliance:>10s}")
    print(f"Wholesale Cost:  ${WholesaleCost:10.2f}")
    print(f"Retail Price:    ${RetailPrice:10.2f}\n")
    print(f"Store Profit:    ${Profit:10.2f}")
    print(f"Sales Commission:${SalesCommission:10.2f}")
    print(f"Sales Tax:       ${SalesTax:10.2f}")
    print(f"Customer Price:  ${TotalCost:10.2f}")
else:
    print("Invalid Appliance Selection")

#End of Applicaiont
print("\nThank you for shopping with us!")
