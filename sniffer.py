def get_user_choice():
    print("Select what to capture:")
    print("1. All packets")
    print("2. Only IP packets")
    print("3. Only TCP packets")
    print("4. Only UDP packets")
    return input("Enter choice (1-4): ").strip()