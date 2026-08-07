print("===========================Zomato===========================================")
print("=======You can order delicious food here from your favorite restaurant======")

while True:

    order_id = int(input("enter id: "))

    if order_id == 1000:
        print("Maximum Ordres Reached.")

        break

    if order_id == 0:
        print("Order ID does not exist.")

        continue

    if order_id == 501:
        print("please skip the order, order is repeated.")

        continue

    if order_id > 1000:
        print("Please consult the Customer Service Team.")

        continue

    if 0 < order_id < 1000:
        print("Your order ID: ")

        customer_name = input("Enter your name:  ")

        order_name = input("Enter your order name: ")

        print(f"Hey {customer_name} , Order ID {order_id} and Order Name : {order_name} is ready to collect. ")

        print("Thank you! Please rate the service.")

print("Restaurant is closed.")

print("Thank you for watching the practice session")

print("Like and Subscribe")

print("See you tomorrow with another concept, Thank you.")

