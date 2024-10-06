# encode_utils.py

# 定义数字到字符的映射表
digit_to_char = {
    '0': 'Z',
    '1': '4',
    '2': '7',
    '3': '}',
    '4': 'S',
    '5': 'K',
    '6': '$',
    '7': '%',
    '8': 'Y',
    '9': '('
}

def encode_number(number_str):
    """
    将17位数字ID转换为自定义编码格式的字符串。
    """
    encoded = []
    for digit in number_str:
        if digit not in digit_to_char:
            raise ValueError(f"无法找到数字 '{digit}' 的映射。请检查映射表。")
        encoded.append(digit_to_char[digit])
    return ''.join(encoded)

def encode_to_hex(encoded_str):
    """
    将编码后的字符串转换为HEX进制编码的字符串。
    """
    return encoded_str.encode('utf-8').hex()
