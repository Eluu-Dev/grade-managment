# Read the CSV file
with open("grades.csv", "rt") as f:
    lines = f.readlines()

# Store (name, score)
students = []
for line in lines[1:]:
    name, score = line.strip().split(",")
    students.append((name, int(score)))

# Calculate average
total = 0
for s in students:
    total += s[1]
average = total / len(students)

# Sort by score (descending)
students = sorted(students, key=lambda x: x[1], reverse=True)

# Write report file
with open("grades_report.txt", "w") as f:
    f.write("Name,Score,Status\n")
    for name, score in students:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        else:
            grade = "C"
        f.write(f"{name},{score},{grade}\n")
    f.write(f"Overall Average: {average}\n")

# Create backup file
try:
    with open("grades_backup.csv", "x") as f:
        f.writelines(lines)
except FileExistsError:
    print("grades_backup.csv already exists")
