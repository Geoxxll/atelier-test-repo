# 用户数据模型

class User:
    def __init__(self, email: str, password_hash: str):
        self.email = email
        self.password_hash = password_hash

    # 其他用户相关的方法可以在这里添加