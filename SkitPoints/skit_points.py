def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = []
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        index = lines[i].strip()
        summed_points = float(lines[i + 1].strip()) if lines[i + 1].strip() and lines[i + 1].strip() != '-' else None
        theory_points = float(lines[i + 2].strip().split()[0]) if lines[i + 2].strip() and lines[i + 2].strip() != '-' else None
        practical_points = float(lines[i + 3].strip().split()[0]) if lines[i + 3].strip() and lines[i + 3].strip() != '-' else None
        group = lines[i + 4].strip()
        if len(index) == 6 and (theory_points is not None and theory_points >= 15) and (practical_points is not None and practical_points >= 10):
            data.append((index, summed_points, theory_points, practical_points, group))
        i += 5
    return data

def write_sorted_files(data):
    groups = {}
    for entry in data:
        _, _, _, _, group = entry
        if group not in groups:
            groups[group] = []
        groups[group].append(entry)

    for group, group_data in groups.items():
        group_data.sort(key=lambda x: x[1] if x[1] is not None else 0, reverse=True)
        with open(f"{group}_sorted.txt", 'w') as file:
            for i, entry in enumerate(group_data, 1):
                index, summed_points, theory_points, practical_points, _ = entry
                file.write(f"Position: {i}\n")
                file.write(f"Index: {index}\n")
                if summed_points is not None:
                    file.write(f"Summed points: {summed_points}\n")
                if theory_points is not None:
                    file.write(f"Theory points: {theory_points}\n")
                if practical_points is not None:
                    file.write(f"Practical points: {practical_points}\n")
                file.write(f"Group: {group}\n\n")

if __name__ == "__main__":
    filename = "skit_results_filtered.txt"
    data = read_data(filename)
    write_sorted_files(data)
    print("Files created with sorted and filtered students.")
