"""
线上巡检 - 检查图片是否加载
"""
import json

from jsonpath import jsonpath
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def check_demo(url):
    # # 使用 ChromeDriverManager 安装 ChromeDriver，并返回驱动程序的路径
    # driver_path = ChromeDriverManager().install()
    # # 打印驱动程序路径
    # print(driver_path)
    # 创建 Chrome WebDriver，并指定驱动路径
    # driver = webdriver.Chrome(executable_path=driver_path)

    caps = DesiredCapabilities.CHROME  # 谷歌浏览器
    caps["goog:loggingPrefs"] = {"performance": "All"}  # 开启获取日志功能 =浏览器官方文档说明
    # driver = webdriver.Chrome(desired_capabilities = caps) # 初始化
    driver = webdriver.Chrome()  # 初始化

    driver.maximize_window()  # 窗口最大化
    # driver.get("www.baidu.com")
    driver.get(url)
    driver.execute_cdp_cmd("Page.reload", {"ignoreCache": True})  # 忽略页面缓存强制刷新获取最新页面
    print("刷新页面")

    log = driver.get_log("performance")
    for i in log:
        # print(i)
        json_log = json.loads(log["message"])
        if json_log["message"]["method"] != "Network.responseReceived":
            continue
        status = jsonpath(json_log,"$.messge.params.response.status")[0]
        if status >= 500:
            driver.save_screenshot("a.png")
            driver.quit()
            raise Exception("线上出问题了！！！")



if __name__ == '__main__':
    check_demo(url="www.baidu.com")
