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


    #     "client_pwd_check": {
    #         "prevent_uninstall": {
    #             "mode": {
    #                 "server": "verification_code_or_static_pwd",
    #                 "modifiable": "0"
    #             },
    #             "enabled": {
    #                 "server": "0",
    #                 "modifiable": "0"
    #             },
    #             "static_pwd": {
    #                 "server": "6aede78b6a20a78a3e0abbe21d00ec4a5dc0b3fd0e8e8a91308887488f0baf1e",
    #                 "modifiable": "0"
    #             }
    #         },
    # 卸载