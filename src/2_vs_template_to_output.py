import zipfile
import os

# 获取当前用户的"文档"路径
documents_path = os.path.expanduser('~\Documents')

# 源文件路径
source_dir = os.path.join(documents_path, 'Visual Studio 2022', 'My Exported Templates')
zip_file_1 = 'WpfMudBlazor.zip'
zip_file_2 = 'WpfMudBlazor.Pages.zip'

# 目标目录
output_dir = 'TemplateOutput'

# 完整的文件路径
zip_file_1_path = os.path.join(source_dir, zip_file_1)
zip_file_2_path = os.path.join(source_dir, zip_file_2)

# 创建目标目录
os.makedirs(output_dir, exist_ok=True)

# 解压第一个压缩文件并将其放入对应的文件夹
with zipfile.ZipFile(zip_file_1_path, 'r') as zip_ref:
    extract_path = os.path.join(output_dir, 'WpfMudBlazor')
    os.makedirs(extract_path, exist_ok=True)
    zip_ref.extractall(extract_path)

# 解压第二个压缩文件并将其放入对应的文件夹
with zipfile.ZipFile(zip_file_2_path, 'r') as zip_ref:
    extract_path = os.path.join(output_dir, 'WpfMudBlazor.Pages')
    os.makedirs(extract_path, exist_ok=True)
    zip_ref.extractall(extract_path)

# 删除原始的两个压缩文件
os.remove(zip_file_1_path)
os.remove(zip_file_2_path)

print("解压完成，并删除原始压缩文件！")
