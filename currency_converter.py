def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
if(current_currency_name=="Euro"):
    current_currency_amount=amount_needed_inr*0.01417
elif(current_currency_name=="British pound"):
    current_currency_amount=amount_needed_inr*0.0100
elif(current_currency_name=="Australian dollar"):
    current_currency_amount=amount_needed_inr*0.02140
elif(current_currency_name=="Canadian dollar"):
    current_currency_amount=amount_needed_inr*0.02027
else:
    current_currency_amount=-1
return current_currency_amount
#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"British pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
