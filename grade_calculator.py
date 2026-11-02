




name = input("Enter student name: ")
print("");

sub1 = int(input("Enter Python Marks: "))
sub2 = int(input("Enter Math Marks: "))
sub3 = int(input("Enter Science Marks: "))
print("")

if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
  print("Invalid Mark");
else:
  pass

average = (sub1 + sub2 + sub3) / 3;

print("")

print(f"Student Name: {name}")
print(f"Average Marks: {average:.2f}")

if average >= 80 and average <= 100:
  print("Final Grade: A+")
elif average >= 70 and average <= 79:
  print("Final Grade: A")
elif average >= 60 and average <= 69:
  print("Final Grade: A-")
elif average >= 50 and average <= 59:
  print("Final Grade: B")
elif average >= 40 and average <= 49:
  print("Final Grade: C")
elif average < 40:
  print("Final Grade: F")