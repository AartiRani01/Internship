role = input("enter your role(admin/manager/operator): ").lower()
login_time = int(input("enter your login time (in hours 0-23): "))
location = input("enter your location (office/remote): ").lower()

if role == "admin":
    print("always allowed")
elif role == "manager":
    if 8 <= login_time <= 20:
        print("always allowed")
elif role == "operator":
    if login_time >= 6 and login_time <= 18 and location == "office":
        print("allowed during office hours from office location")
    else: 
        print("not allowed")

