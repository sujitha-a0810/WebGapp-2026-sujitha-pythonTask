phone_book = {}
while True:
    print("\n--- Phone Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")
        phone_book[name] = number
        print("Contact Added Successfully")
    elif choice == "2":
        if len(phone_book) == 0:
            print("Phone Book is Empty")
        else:
            print("\nContacts:")
            for name, number in phone_book.items():
                print(name, ":", number)
    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in phone_book:
            print("Phone Number:", phone_book[name])
        else:
            print("Contact Not Found")
    elif choice == "4":
        name = input("Enter Name to Update: ")
        if name in phone_book:
            new_number = input("Enter New Number: ")
            phone_book[name] = new_number
            print("Contact Updated")
        else:
            print("Contact Not Found")
    elif choice == "5":
        name = input("Enter Name to Delete: ")
        if name in phone_book:
            del phone_book[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")
    elif choice == "6":
        print("Exiting Phone Book...")
        break
    else:
        print("Invalid Choice")