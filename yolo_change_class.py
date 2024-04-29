import os
import re
 
# 定义一个函数，用于处理单个文件
def process_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
 
    modified_lines = []
 
    for line in lines:
        if re.match(r'^1', line.strip()):
            # 找到以2开头的行，替换第一个数字为1
            parts = line.strip().split(' ')
            if len(parts) > 1:
                parts[0] = '2'
                modified_line = ' '.join(parts)
                modified_lines.append(modified_line + '\n')
            else:
                # 行中只有一个数字2，不作处理
                modified_lines.append(line)
        else:
            modified_lines.append(line)
 
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
 
# 定义一个函数，用于处理整个文件夹
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_txt_file(file_path)
                print(f"Processed: {file_path}")
 
# 指定要处理的文件夹目录
folder_to_process = "/media/jim/drow_data"  # 替换成你的文件夹路径
 
# 调用函数来处理文件夹中的txt文件
process_folder(folder_to_process)

