import csv
import random
import os


def read_csv(filename):
    """
    Read CSV file and return a list of dictionaries containing student data.
    """
    students = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students


def write_csv(filename, data):
    """
    Write data to CSV file.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def distribute_groups(students, group_size, strict_group=False):
    """
    Distribute students into groups of specified size, ensuring at least one lady per group.
    """
    random.shuffle(students)
    groups = []
    num_groups = len(students) // group_size
    remainder = len(students) % group_size

    for i in range(num_groups):
        group = []
        for j in range(group_size):
            student = students.pop()
            if student['gender'] == 'female':
                group.append(student)
            else:
                group.insert(random.randint(0, len(group)), student)
        groups.append(group)

    # Add remaining students to last group
    if not strict_group and remainder > 0:
        last_group = groups[-1]
        for _ in range(remainder):
            student = students.pop()
            if student['gender'] == 'female':
                last_group.append(student)
            else:
                last_group.insert(random.randint(0, len(last_group)), student)

    # Add remaining students to new group
    if strict_group and remainder > 0:
        group = []
        for _ in range(remainder):
            student = students.pop()
            group.append(student)
        groups.append(group)

    return groups


def main():
    filename = 'students.csv'

    # Check if students.csv exists
    if not os.path.isfile(filename):
        print("Error: students.csv file not found.")
        return

    # Read CSV file
    students = read_csv(filename)

    # Get group size from user input
    while True:
        try:
            group_size = int(input("Enter the number of students per group: "))
            if group_size <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    # Ask if strict group size is desired
    input_strict = input("Do you want strict group size? (yes/no): ").lower()
    strict_group = input_strict == 'yes' or input_strict == 'y'

    # Distribute groups
    groups = distribute_groups(students, group_size, strict_group)

    # Display line
    print("\n-----*-----\n")

    # Output group distribution
    for i, group in enumerate(groups):
        print(f"Group n° {i + 1} with {len(group)} students:")
        for student in group:
            print(f"{student['first_name']} {student['last_name']} ({student['section']})")
        print()


if __name__ == "__main__":
    main()
