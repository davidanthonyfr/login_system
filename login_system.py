# Step 1: Store a username and password
USERNAME = "admin"
PASSWORD = "1234"

# Step 2: Allow 3 attempts
attempts = 3

while attempts > 0:
    # Step 3: Ask the user for login details
    user = input("Enter username: ")
    pw = input("Enter password: ")

    # Step 4: Check credentials
    if user == USERNAME and pw == PASSWORD:
        print("✅ Login successful! Welcome,", user)
        break
    else:
        attempts -= 1
        print("❌ Wrong credentials. Attempts left:", attempts)

# Step 5: Lockout if no attempts remain
if attempts == 0:
    print("⛔ Account locked. Too many failed attempts.")
