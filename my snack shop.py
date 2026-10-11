snack_name  ="chips"
price       =1.50
quantity    =10
is_available = True

print("Snack Name:", snack_name)
print("Price: $", price)
print("Quantity:", quantity)
print("Is Available:", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))


total= price * quantity
print("Total Cost: $", total)
print("Sale price: $", price - 0.25)
print("Double stock: ", quantity * 2)


print("Is price under $2.00?", price < 2.00)
print( "More than 5 in stock?", quantity > 5)
print("Is price exactly $1.50 and available?", price == 1.50)

shop_name = "quick" + " " + "Bites"
print("Shop Name:", shop_name)
print("Letters in snack name:", len(snack_name))
print("First letter of snack name:", snack_name[0])

price_a = 1.50
price_b = 3.00
print("Before:" , price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After:" , price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After" , price_a, "and", price_b)
