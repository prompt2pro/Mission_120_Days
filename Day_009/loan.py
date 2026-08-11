print("======================Bank Loan======================")

banks = ("SBI", "HSBC","HDFC", "Natwest", "Monzo", "BOB", "BOI", "Barclays", "Revolut")

total_banks = len(banks)

bank_status = []

for bank in banks:

    while True:

        status = input(f"Choose Bank Approval Status 'approved' or 'pending' : {bank} :  ").strip().lower()

        if status == "approved" or status == "pending":
            break
        else:
            print("Choose either 'approved' or 'pending' ")

    bank_status.append(status)

    print(f"Bank Name : {bank}  Status : {status}")

print("==========================================================================================")

total_banks = len(banks)

print(f"Total Banks : {total_banks}")


approved = bank_status.count("approved")
pending = bank_status.count("pending")

print(f"Approved : {approved}")
print(f"Pending : {pending}")

approved_percentage = approved/total_banks*100
pending_percentage = pending/total_banks*100

print(f"Bank Loan Approval Percentage : {approved_percentage: .2f}%")
print(f"Bank Loan Pending Percentage : {pending_percentage: .2f}%")

print("============================================================")

print("=================Bank Loan Analysis Report==================")