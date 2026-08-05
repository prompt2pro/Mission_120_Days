print("===================Netflix====================")
name = input("Enter your name:  ")
email_id = input("Enter your email id = ")
password = input("Enter your password: ")

if name == "" or email_id == "" or password == "":
       print("Please fill in the details to create an account.")
else:
       print("Successfully Logged in.")
       print(f"Hey {name} Happy to see you again in the Netflix.")

membership_status = input("Choose your membership status: ")

if membership_status == "active":
       print("You are ready to watch your netflix favorite shows.")
else:
       print("Please activate your membership.")

payment_status = input("Enter your payment status: ")

if payment_status == "paid":
       print("Enjoy the Netflix services")
elif payment_status == "non paid":
       print("Check the payment status")
else:
       print("You are not an active member.")

approval_status = input("Enter your approval status: ")

if approval_status == "approved":
       print("Enjoy the streaming.")
else:
       print("Your approval is pending.")

if (name != "" 
    and email_id != "" 
    and password != "" 
    and membership_status == "active" 
    and payment_status == "paid"
    and approval_status == "approved"):
  
  print(f"Hey {name} Netflix shows are available for you, congratuations.")
else: 
  print("Please fill the necessary fields. thank you. You are not an active member so we have cancelled your approval status.")

print(f"======Hey {name} thanks for choosing Netflix.======")