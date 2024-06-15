import json


def read_json(path):
    # 读取 JSON 文件
    with open(path, 'r') as file:
        data = json.load(file)
        print(data)
    # 访问和打印特定的值
    value = data["client_pwd_check"]["prevent_exit"]["enabled"]["server"]
    print("value:", value)
    return value


def revise_json(path, value="0"):
    # 读取 JSON 文件
    with open(path, 'r') as file:
        data = json.load(file)
    data['client_pwd_check']['prevent_exit']['enabled']['server'] = value
    # 将修改后的内容写回文件
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)


def update_json(path):
    result = read_json(path)
    if result != "0":
        print("需要修改！！！")
        revise_json(path)
    else:
        print("不需要修改")

if __name__ == '__main__':

    path = r"/Users/Shared/QI-ANXIN Tianqing/Config/setting/software_qi-anxin-tianqing_config_base.json"
    update_json(path)
