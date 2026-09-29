with open("file1.txt", "w") as f:
    f.write("Line1\nLine2\nLine3\nLine4\nLine5\n")
with open("file2.txt", "w") as f:
    f.write("A\nB\nC\n")
f1_lines = open("file1.txt", "r").readlines()
f2_lines = open("file2.txt", "r").readlines()
mid_index = len(f1_lines) // 2
last_index = len(f2_lines) - 1
print(f"Before Swap: File1 Middle={f1_lines[mid_index].strip()}, File2 Last={f2_lines[last_index].strip()}")
temp = f1_lines[mid_index]
f1_lines[mid_index] = f2_lines[last_index]
f2_lines[last_index] = temp
open("file1.txt", "w").writelines(f1_lines)
open("file2.txt", "w").writelines(f2_lines)
print("After Swap Done! Check files.")
