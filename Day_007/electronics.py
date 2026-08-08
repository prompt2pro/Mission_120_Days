print("====================Amazon================")
print("================Amazon Bill Receipt=======")

iphone = 2758
samsung = 2354
oppo = 1935
lg = 1876
mi = 1540
google = 1768
air_pods = 4850

total_bill = 0

while True:

    item_name = input("Enter item name or 'finish' to complete the purchase:  ").strip().lower()

    if item_name == "finish":
        print("Thank you.")
        break

    elif item_name == "iphone":
        total_bill = total_bill + iphone

        print(f"Iphone Price : {iphone}")

    elif item_name == "samsung":
        total_bill = total_bill + samsung

        print(f"Samsung Price : {samsung}")

    elif item_name == "oppo":
        total_bill = total_bill + oppo

        print(f"Oppo Price : {oppo}")

    elif item_name == "lg":
        total_bill = total_bill + lg

        print(f"LG Price : {lg}")

    elif item_name == "mi":
        total_bill = total_bill + mi

        print(f"MI Price : {mi}")

    elif item_name == "google":
        total_bill = total_bill + google

        print(f"GOOGLE Price : {google}")

    elif item_name == "air_pods":

        total_bill = air_pods + total_bill

        print(f"Air_Pods Price : {air_pods}")

    else:
      print("Sorry not available.")

print("Thank you for shopping! Amazon!")

print(f"Total Bill : {total_bill}")

print("Thank you for the payment.")

print("Thank you for watching and please like and subscribe, see you in another session with a new concept and a new project.")
