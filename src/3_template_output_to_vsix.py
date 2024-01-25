import zipfile
import os

def zip_directory(directory, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)
                zipf.write(file_path, arcname=arcname)

# 文件夹路径
folder_path = "TemplateOutput"

# 压缩文件夹路径
zip_folder_path = "WpfMudBlazorTemplate\WpfMudBlazorTemplate\ProjectTemplates"

# 压缩文件路径
zip_file_path = os.path.join(zip_folder_path, "WpfMudBlazorTemplate.zip")

# 如果压缩文件夹不存在，则创建
if not os.path.exists(zip_folder_path):
    os.makedirs(zip_folder_path)

# 调用函数进行压缩
zip_directory(folder_path, zip_file_path)

print(f'文件夹"{folder_path}"中的内容已成功压缩到"{zip_file_path}"文件。')
