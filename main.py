import os, json

# 导出资源的路径
resource_path = "prefab"

# 输出的json文件名
output_file = "img_data.json"

# 导出资源类型 img prefab
output_type = "prefab"


def init():
    global resource_path
    global output_file
    global output_type
    params = input().split()
    resource_path = params[0]
    output_file = params[1]
    output_type = params[2]
    print(f'导出资源的路径 {resource_path}\n')
    print(f'输出的json文件名 {output_file}\n')
    print(f'导出资源类型 {output_type}\n')


def main():
    prefabs = {}
    # 遍历资源文件夹
    need_files = os.walk(resource_path)
    # class_prefab = "//---该文件由PathJson.py自动生成，请勿手动修改---\n\n"
    # 遍历prefab文件夹及所有子文件夹
    for root, dirs, files in need_files:
        for file in files:
            if (output_type == "img"):
                # 检查文件是否为图片格式
                if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                    # 获取图片的路径
                    prefab_path = os.path.join(root, file).replace('\\', '/')
                    # 获取名字
                    file_name = os.path.basename(prefab_path).replace(".lh", "")
                    # 将图片路径保存到字典中
                    prefabs.update({file_name: prefab_path})
                    # 添加新键值 不会更新已有键值
                    # prefabs.setdefault(file_name, prefab_path)
                    print(f'Success update Resources --------------------  {file_name} ：{prefab_path}')
            elif (output_type == "prefab"):
                # 检查文件是否为预设格式
                if file.endswith('.lh'):
                    # 获取图片的路径
                    prefab_path = os.path.join(root, file).replace('\\', '/')
                    # 获取名字
                    file_name = os.path.basename(prefab_path).replace(".lh", "")
                    # 将图片路径保存到字典中
                    prefabs.update({file_name: prefab_path})
                    # 添加新键值 不会更新已有键值
                    # prefabs.setdefault(file_name, prefab_path)
                    print(f'Success update Resources --------------------  {file_name} ：{prefab_path}')

    # 将prefabs列表中的内容写入到json文件中
    with open(output_file, "w", encoding='utf-8') as f:
        # f.write(class_prefab)
        json.dump(prefabs, f)

    print(f"资源已导出并写入到 {output_file}")


init()
main()
