def bit_to_bool(bit_value):
    """
    将 MySQL BIT(1) 类型转换为 Python 布尔值
    
    Args:
        bit_value: 从数据库获取的 BIT 值
        
    Returns:
        bool: 转换后的布尔值
    """
    if bit_value is None:
        return None
    
    # 如果是字节类型，检查是否为 b'\x01'
    if isinstance(bit_value, bytes):
        return bit_value == b'\x01'
    
    # 如果已经是布尔类型，直接返回
    if isinstance(bit_value, bool):
        return bit_value
    
    # 其他情况尝试转换为整数再判断
    try:
        return bool(int(bit_value))
    except (ValueError, TypeError):
        # 无法转换时返回原值
        return bit_value