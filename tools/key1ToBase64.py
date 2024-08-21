import os
import json
import base64

# 定义文件夹和输出文件名
folder_name = "my_secret"
secret_file_name = "secret.txt"

# 获取文件夹内文件列表
files = os.listdir(folder_name)

# 查找 JSON 文件
json_files = [f for f in files if f.endswith(".json")]

# 检查文件夹内是否只有一个 JSON 文件
if len(json_files) == 1:
    # 获取 JSON 文件名
    json_file_name = json_files[0]

    # 构造 JSON 文件的完整路径
    json_file_path = os.path.join(folder_name, json_file_name)

    # 读取 JSON 文件内容
    with open(json_file_path, "r") as f:
        json_data = json.load(f)

    # 将 JSON 数据转换为 Base64 编码
    secret_data = base64.b64encode(json.dumps(json_data).encode()).decode()

    # 将 Base64 编码后的数据写入 secret.txt 文件
    with open(os.path.join(folder_name, secret_file_name), "w") as f:
        f.write(secret_data)

    print(f"已成功将 {json_file_name} 转换为 {secret_file_name}")
else:
    print("错误：文件夹内必须只有一个 JSON 文件")