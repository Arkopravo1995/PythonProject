def ticket_cost(no_of_adults ,no_of_children):
    at_price = 37550.0
    child_p = at_price/3
    amount = (at_price*no_of_adults+child_p*no_of_children)
    s_tax = ((amount)*(7/100))
    all_amount = s_tax+amount
    discount = ((all_amount)*(10/100))
    total = (all_amount-discount)
    return total
result =ticket_cost(1,3)
print(result)