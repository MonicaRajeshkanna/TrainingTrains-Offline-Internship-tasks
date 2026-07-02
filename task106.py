months = int(input("Months as Customer: "))
complaints = int(input("Number of Complaints: "))

if complaints > 3:
    print("High Churn Risk")
else:
    print("Low Churn Risk")