import os
import shutil


def copy_and_replace(src_folder, dest_folder, search_string, replace_string):

    print("Started.")
    # 删除目标文件夹的内容
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)

    # 复制源文件夹到目标文件夹
    shutil.copytree(src_folder, dest_folder,
                    ignore=shutil.ignore_patterns('.vs', 'bin', 'obj'))

    # 遍历目标文件夹中的文件
    for root, dirs, files in os.walk(dest_folder):
        for file in files:
            if file.endswith(".sln"):
                continue
            file_path = os.path.join(root, file)

            # 执行字符串替换
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if search_string in content:
                print(f"Found '{search_string}' in {file_path}")
                content = content.replace(search_string, replace_string)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

    print("Task completed.")


if __name__ == "__main__":
    source_folder = "WpfMudBlazor"
    destination_folder = "TemplateCode"
    search_string = "WpfMudBlazor"
    replace_string = "$safeprojectname$"

    copy_and_replace(source_folder, destination_folder,
                     search_string, replace_string)
