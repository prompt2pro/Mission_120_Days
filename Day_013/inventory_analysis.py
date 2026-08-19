print("========================================================")
print("        Inventory Analysis & SLA Tracker                ")
print("========================================================")

def estimate_reorder_point(daily_demand,lead_time,safety_stock):
    reorder_point = (daily_demand * lead_time) + safety_stock
    return reorder_point

def estimate_order_quantity(maximum_stock,current_stock):
    order_quantity = (maximum_stock - current_stock)
    return order_quantity

def calculate_days_cover(current_stock, daily_demand):
    days_cover = (current_stock/daily_demand)
    return days_cover

products = []

reorder_count = 0
healthy_count = 0
overstock_count = 0
sla_risk_count = 0

while True:

    print("====================Product Entry====================")

    sku = input("Enter SKU: ").strip().upper()
    product_name = input("Enter product name: ").strip().upper()
    category = input("Enter category: ").strip().upper()
    current_stock = int(input("Enter Current Stock: "))
    daily_demand = int(input("Enter daily demand: "))
    lead_time = int(input("Enter Lead Time: "))
    safety_stock = int(input("Enter Safety Stock: "))
    maximum_stock = int(input("Enter Maximum Stock: "))

    reorder_point = estimate_reorder_point(daily_demand,lead_time,safety_stock)

    days_cover = calculate_days_cover(current_stock,daily_demand)



    if current_stock > maximum_stock:

        inventory_status = "Overstock"
        action = "Do not Order"
        order_quantity = 0

        overstock_count += 1

    elif current_stock <= reorder_point:
        inventory_status = "Order again"

        order_quantity = estimate_order_quantity(maximum_stock,current_stock)

        action = f"Order {order_quantity} Units"

        reorder_count +=1

    else:
        inventory_status = "Healthy Stock"
        action = "No Order required at the moment"
        order_quantity = 0

        healthy_count += 1




    if days_cover <= lead_time:

        availability_status = "SLA Risk"
        sla_risk_count += 1

    else:

        availability_status = "Covered"

    product_record  = {
    "sku" : sku,
    "product": product_name,
    "category": category,
    "current_stock": current_stock,
    "daily_demand": daily_demand,
    "lead_time": lead_time,
    "safety_stock": safety_stock,
    "maximum_stock": maximum_stock,

    "reorder_point": reorder_point,
    "days_cover": days_cover,
    "inventory_status": inventory_status,
    "order_quantity" : order_quantity,
    "availability_status": availability_status

    }

    products.append(product_record)

    print("===============================Inventory Analysis=========================")

    print(f"SKU : {sku}")
    print(f"Product : {product_name}")
    print(f"Category : {category}")
    print(f"Current Stock : {current_stock}")
    print(f"Daily Demand : {daily_demand}")
    print(f"Lead Time : {lead_time}")
    print(f"Saftey Stock : {safety_stock}")
    print(f"Maximum Stock : {maximum_stock}")
    print(f"Reorder Point : {reorder_point}")
    print(f"Days of Stock Cover : {days_cover:.2f}")

    print(f"Inventory Status : {inventory_status}")

    print(f"Order Quantity : {order_quantity}")

    print(f"Availabitlity Staus : {availability_status}")

    print("=============================================================================")

    continue_analysis = input("Do you want to analyse another product? yes/no: ").strip().lower()

    if continue_analysis == "no":
        break


print("=============================================================================")

print("=============================Final Inventory Summary                         ")

print("==============================================================================")

print(f"Total Products Analysed : {len(products)}")
print(f"Reorder Required : {reorder_count}")
print(f"Healthy stock: {healthy_count}")
print(f"Overstocked Products: {overstock_count}")
print(f"SLA Risk Products: {sla_risk_count}")

print("==========================Products Summary====================================")

for product in products:

    print("===========================================================================")

    print(f"SKU : {product['sku']}")
    print(f"Product : {product['product']}")
    print(f"Category : {product['category']}")
    print(f"Current Stock : {product['current_stock']}")
    print(f"Reorder Point : {product['reorder_point']}")
    
    print(f"Inventory Status : {product['inventory_status']}")
    print(f"Order Quantity : {product['order_quantity']}")


    
    print(f"Availabitlity Staus : {product['availability_status']}")


print("=====================================================================================")

print("=================Inventory Analysis Complete=========================================")

print("======================================================================================")




    



    
