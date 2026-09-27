phone_book = {"Tarana": "9876543210","Khushi": "9123456789","Unzila": "9988776655"}
name = input("Enter name to search: ")
if name in phone_book:
    print("Phone number of", name, "is", phone_book[name])
else:
    print("Name not found!")
