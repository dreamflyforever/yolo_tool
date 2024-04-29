import os
 
# 定义一个函数，用于处理单个文件
def process_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
 
    # 过滤掉以"1"开头的行
    filtered_lines = [line for line in lines if not line.strip().startswith("0")]
 
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)
 
# 定义一个函数，用于处理整个文件夹
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_txt_file(file_path)
                print(f"Processed: {file_path}")
 
# 指定要处理的文件夹目录
#folder_to_process = "/media/jim/eye6" # 替换成你的文件夹路径
folder_to_process = "/media/jim/drow_data" # 替换成你的文件夹路径
 
# 调用函数来处理文件夹中的txt文件
process_folder(folder_to_process)
