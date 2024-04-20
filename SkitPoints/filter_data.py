def filter_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    filtered_lines = []
    skip_next_empty_line = False
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            if skip_next_empty_line:
                skip_next_empty_line = False
                continue
            else:
                continue
        if '-' in line_stripped:
            line_stripped = line_stripped.replace('-', '0')
        filtered_lines.append(line_stripped)
        skip_next_empty_line = True
    return filtered_lines

def write_filtered_data(filtered_lines, output_filename):
    with open(output_filename, 'w') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    input_filename = "skit_results_unfiltered.txt"
    output_filename = "skit_results_filtered.txt"
    filtered_lines = filter_lines(input_filename)
    write_filtered_data(filtered_lines, output_filename)
    print("Filtered data written to", output_filename)
