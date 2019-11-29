def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    if(no_of_five > five_needed and no_of_one > one_needed):
        five_needed = no_of_five - rupees_to_make % 5
        one_needed = rupees_to_make % 5
    rupees_to_make = five_needed * 5 + one_needed * 1

    print("No. of Five needed :", five_needed)
    print("No. of One needed  :", one_needed)
    print(-1)
make_amount(21,5,1)
