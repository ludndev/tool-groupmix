# GroupMix

GroupMix is a Python script that helps distribute students into groups while ensuring diversity and fairness. It reads student data from a CSV file, shuffles the data, and then distributes the students into groups of the specified size. Additionally, it provides an option to enforce strict group size, ensuring each group has an equal number of students whenever possible.

## Features

- **Group Distribution:** Distribute students into groups of specified size.
- **Diversity:** Ensure that there is at least one female student per group.
- **Strict Group Size:** Optionally enforce strict group size, ensuring an equal number of students in each group whenever possible.

## How to Use

1. **Prepare Student Data:**
   - Create a CSV file named `students.csv` containing student data with columns for ID, first name, last name, section, and gender.

2. **Run the Script:**
   - Execute the `main.py` script.
   - Follow the prompts to specify the number of students per group and whether to enforce strict group size.

3. **View Group Distribution:**
   - The script will output the distribution of students into groups, ensuring diversity and fairness.

## Requirements

- Python 3.x
- CSV file containing student data

## Usage Example

```bash
python main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
