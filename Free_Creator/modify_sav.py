# modify_sav.py
from config import SEARCH_STRING

def replace_bytes_in_sav(file_path, replacement_hex):
    # 将替换字节转换为字节类型
    replacement = bytes.fromhex(replacement_hex)
    
    # 读取文件内容
    with open(file_path, "rb") as f:
        data = f.read()
    
    # 查找所有匹配的位置
    positions = []
    start = 0
    while True:
        pos = data.find(SEARCH_STRING, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + len(SEARCH_STRING)
    
    # 检查找到的匹配数量
    if len(positions) < 3:
        raise ValueError("文件中找到的 'SafeString' 数量不足三个")
    
    # 打印找到的所有位置
    print(f"找到的 'SafeString' 位置: {positions}")

    # 定位第一个"SafeString"后的第56个字节并替换
    first_position = positions[0] + len(SEARCH_STRING) + 56
    print(f"将要替换第一个位置: {first_position}")

    # 确保替换后内容长度匹配
    if first_position + len(replacement) > len(data):
        raise ValueError("替换位置超出了数据范围")

    # 替换数据
    data = data[:first_position] + replacement + data[first_position + len(replacement):]

    # 定位第三个"SafeString"后的第57个字节并替换
    third_position = positions[2] + len(SEARCH_STRING) + 57
    print(f"将要替换第三个位置: {third_position}")

    # 再次确保替换后内容长度匹配
    if third_position + len(replacement) > len(data):
        raise ValueError("替换位置超出了数据范围")

    # 替换数据
    data = data[:third_position] + replacement + data[third_position + len(replacement):]

    # 写入修改后的数据回文件
    with open(file_path, "wb") as f:
        f.write(data)

    print(f"文件 {file_path} 已成功修改。")

    # 验证文件内容是否已修改
    with open(file_path, "rb") as f:
        modified_data = f.read()
        if modified_data != data:
            print("警告: 文件内容与修改后的内容不一致！")
        else:
            print("文件内容已成功更新。")