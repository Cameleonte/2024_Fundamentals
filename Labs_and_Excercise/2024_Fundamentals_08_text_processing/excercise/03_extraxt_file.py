file_path = input().split('\\')

name_path = file_path[-1]
file_name, file_extension = name_path.split('.')
print(f'File name: {file_name}\nFile extension: {file_extension}')
