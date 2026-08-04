print("======================Flight Ticket Booking==========================")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
gender = input("Enter your gender: ")
birth_year = int(input("Enter your birth year: "))
nationality = input("Enter your nationality: ")
origin_country = input("Enter your origin country: ")
destination_country = input("Enter your desintation country: ")
flight_name = input("Chooser your flight: ")
flight_number = int(input("Enter flight number: "))
seat_allocated = int(input("Choose your seat number: "))

adults_number = int(input("Enter number of passengers: "))
child_number = int(input("Enter number of children: "))
total_persons = adults_number + child_number

adult_price = int(1500)
child_price = int(750)

total_adult_price = adults_number * adult_price
total_child_price = child_number * child_price

total_price = total_adult_price + total_child_price

payment_status = input("Enter payment status: ")

print(f"My name is {first_name} {last_name} and I am from {nationality} and my birth year is {birth_year} and I am {gender}." )
print(f"Travelling from {origin_country} to {destination_country}.")
print(f"My flight name is {flight_name} and flight number is {flight_number} and the seat number is {seat_allocated}.")
print(f"number of adults are travelling {adults_number}.")
print(f"number of children are travelling {child_number}.")

print(f"Total number of persons: {total_persons}.")

print(f"each adult price is : {adult_price}.")
print(f"each child price is : {child_price}.")

print(f"total price of adults : {total_adult_price}")
print(f"total price of children: {total_child_price}")

print(f"total fair is : {total_price}.")

print(f"please tell me your payment status: {payment_status}")

print("=======================Happy Journey=============================")
print("=======================Successfully Flight Ticket Generated===========")
print("==============Here are your Itenary Details=======================")
print(f"{first_name} {last_name}")
print(f"from {origin_country} to {destination_country}.")
print((f"Adults: {adults_number} Children: {child_number}"))
print("==============Payment accepted, Have a Safe Journey===========")
print("======================Thank you=============================")