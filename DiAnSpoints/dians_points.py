import os
import re

def extract_and_sort_by_grade(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Use regular expression to extract both columns
    pattern = re.compile(r'(\d+)\s+([\d.]+)')
    matches = pattern.findall(text)

    # Create a list of tuples (index, grade)
    data = [(int(index), float(grade)) for index, grade in matches]

    # Sort the list based on the second column (grades)
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

    return sorted_data

def write_sorted_output(sorted_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for index, points in sorted_data:
            output_file.write(f"Index: {index}, Points: {points}\n")

def count_students(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Use regular expression to find all student entries
    pattern = re.compile(r'\d+\s+[\d.]+')
    matches = pattern.findall(text)

    # Count the number of student entries
    num_students = len(matches)

    return num_students

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(script_dir, "unsorted_input.txt")
    output_path = os.path.join(script_dir, "sorted_output.txt")

    sorted_data = extract_and_sort_by_grade(txt_path)

    # Write the sorted list to the output file
    write_sorted_output(sorted_data, output_path)

    # Count the number of students
    num_students = count_students(txt_path)
    print(f"Number of students: {num_students}")
    print(f"Sorted output has been written to {output_path}")
