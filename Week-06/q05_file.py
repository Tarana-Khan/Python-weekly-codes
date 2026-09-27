n = int(input("How many students? "))
with open("Marks.data", "w") as f:
    for i in range(n):
        roll = input(f"\nEnter roll no of student {i+1}: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        f.write(f"{roll}, {name}, {marks}\n")
print("\nData saved in Marks.data successfully!")
