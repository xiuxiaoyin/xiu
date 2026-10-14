#存放工具函数

import yaml

def load_cases(path):
    #读取一个 YAML 文件，并把它解析成 Python 对象（通常是字典或列表）返回
    with open(path,encoding="utf-8") as f:
        return yaml.safe_load(f)
