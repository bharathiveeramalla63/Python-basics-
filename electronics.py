print("electronicdevices")
mobile=12000
quantity1=2
laptop=80000
quantity2=1
tv=50000
quantity3=1
cost_of_mobiles=mobile*quantity1
cost_of_laptop=laptop*quantity2
cost_of_tv=tv*quantity3
total_cost=cost_of_mobiles+cost_of_laptop+cost_of_tv
discount_rate=10
total_discount=total_cost*10/100
total_bill=total_cost-total_discount
print(f"discount on electronics:{discount_rate}%")
print(f"mobile:{mobile},quantity:{quantity1}")
print(f"laptop:{laptop},quantity:{quantity2}")
print(f"tv:{tv},quantity:{quantity3}")
print(f"total_cost:{total_cost}")
print(f"total discount on items:{total_discount}")
print(f"amount:{total_bill}")
print(f" you get discount {discount_rate}% on electronic devices such as mobile,laptop,and tv")