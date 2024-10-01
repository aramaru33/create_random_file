import os
import random
import string
import argparse

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_random_file_structure(seed, num_files, base_dir='.', max_depth=3, max_files_per_folder=5):
    random.seed(seed)
    
    def create_files_and_folders(current_path, current_depth, current_file_num):
        if current_depth > max_depth:
            return
        if current_file_num > num_files:
            return
        
        # Create random number of files in the current folder
        num_files_in_folder = random.randint(1, max_files_per_folder)
        for _ in range(num_files_in_folder):
            file_name = generate_random_string(random.randint(1, 20)) + '.txt'
            file_path = os.path.join(current_path, file_name)
            file_content = generate_random_string(random.randint(20, 100))
            with open(file_path, 'w') as file:
                file.write(file_content)
            print(f'Created file: {file_path}')
            current_file_num += 1
            if current_file_num > num_files:
                return
        
        # Create random number of subfolders in the current folder
        num_subfolders = random.randint(1, max_files_per_folder)
        for _ in range(num_subfolders):
            folder_name = generate_random_string(random.randint(1, 20))
            folder_path = os.path.join(current_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            create_files_and_folders(folder_path, current_depth + 1, current_file_num)
    
    create_files_and_folders(base_dir, 1, 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create random text files in random directories.')
    parser.add_argument('seed', type=int, help='Seed value for random number generator')
    parser.add_argument('num_files', type=int, help='Number of files to create')
    parser.add_argument('--max_depth', type=int, default=3, help='Maximum depth of directories')
    parser.add_argument('--max_files_per_folder', type=int, default=5, help='Maximum number of files per folder')
    args = parser.parse_args()
    
    create_random_file_structure(args.seed, args.num_files, max_depth=args.max_depth, max_files_per_folder=args.max_files_per_folder)
