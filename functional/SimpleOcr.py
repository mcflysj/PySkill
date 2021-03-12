'''
设置百度ocr api信息可识别剪贴板图片并整理、
也可识别制定路径图片，不指定路径则默认识别剪贴板图片
识别后输出并存入剪贴板
'''
from aip import AipOcr
from PIL import ImageGrab
import pyperclip

config = {
    'appId': '你的appid',
    'apiKey': '你的apikey',
    'secretKey': '你的秘钥'
}

client = AipOcr(**config)


# 获取文件或剪贴板
def get_file_content(file):
    if not file:
        img = ImageGrab.grabclipboard()
        try:
            img.save("tmp.png", "PNG")
        except:
            return None
        else:
            file = "tmp.png"
    try:
        with open(file, 'rb') as fp:
            return fp.read()
    except:
        return None
    else:
        pass


# 文件转文字
def img_to_str(image_path):
    image = get_file_content(image_path)
    if image:
        # 通用文字识别（可以根据需求进行更改）
        results = client.basicGeneral(image)
        return results["words_result"]


# 文字分段落
def format_paragraph(results):
    # 分段转储为list 并在分段后第一行加空格
    if not results:
        return None
    text = str()  # 合并后的字符串
    fix_num = 4  # 修正字符数
    words_max = 0  # 字最多的一行
    if input("默认自动分段，任意键取消，回车继续\n"):
        for result in results:
            text += str(result["words"]) + "\n"
        return text
    for i in range(len(results)):
        results[i]["count"] = len(results[i]["words"])
        if words_max < results[i]["count"]:
            words_max = results[i]["count"]
    # 判断行头、行尾
    for i in range(len(results)):
        if words_max - results[i]['count'] > fix_num:
            text += str(results[i]["words"]) + "\n    "
        else:
            text += str(results[i]["words"])
    return text


if __name__ == "__main__":
    while True:
        path = input("\n拖入图片或回车识别剪贴板内容：\n")
        results = img_to_str(path)
        text = format_paragraph(results)
        if text:
            print("-----------------------------\n%s" % (text))
            pyperclip.copy(text)
            print("-----------------------------\n[已拷贝至剪贴板]\n")
        else:
            print("[输入有误]\n")
