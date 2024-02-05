import os


def get_files_info(folder_path):
    files_info = []  # Renamed variable
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            files_info.append((file, file_size))
    return files_info


def save_to_file(file_info, output_file):
    with open(output_file, 'w') as f:
        for file, size in file_info:
            f.write(f"{file},{size}\n")


def find_largest_file(files_size):  # Renamed parameter
    largest_file = max(files_size, key=lambda x: x[1])
    return largest_file


if __name__ == "__main__":
    current_folder = os.getcwd()
    files_info_list = get_files_info(current_folder)  # Renamed variable
    save_to_file(files_info_list, "files_size.txt")

    largest_file_name, largest_file_size = find_largest_file(files_info_list)  # Renamed variable
    print(f"Largest file: {largest_file_name}, Size: {largest_file_size} bytes")
