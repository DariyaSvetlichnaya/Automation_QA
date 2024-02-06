import os


def get_files_info(folder_path):
    files_info = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            files_info.append((file_path, file, file_size))  # Include file path
    return files_info


def save_to_file(file_info, output_file):
    with open(output_file, 'w') as f:
        for file_path, file, size in file_info:
            f.write(f"{file_path},{size}\n")  # Write file path


def find_largest_file(files_info):
    largest_file = max(files_info, key=lambda x: x[2])  # Compare by size
    file_path, file_name, file_size = largest_file
    file_name_without_extension = os.path.splitext(file_name)[0]  # Remove extension
    return file_path, file_name_without_extension, file_size  # Return file path, name without extension, and size


if __name__ == "__main__":
    current_folder = os.getcwd()
    files_info_list = get_files_info(current_folder)
    save_to_file(files_info_list, "files_size.txt")

    largest_file_path, largest_file_name, largest_file_size = find_largest_file(files_info_list)
    print(f"Largest file: {largest_file_name}, Path: {os.path.relpath(largest_file_path)}, Size: {largest_file_size} bytes")
