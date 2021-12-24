import os
import cv2
from PIL import Image, ImageDraw
from datetime import datetime

"""
 detectFaces()返回图像中所有人脸的矩形坐标（矩形左上、右下顶点）
"""


def detectFaces(image_name):
    img = cv2.imread(image_name)
    face_cascade = cv2.CascadeClassifier(os.getcwd() + "\\..\\file\\haarcascade_frontalface_alt.xml")
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img  # if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)  # 1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []
    for (x, y, width, height) in faces:
        result.append((x, y, x + width, y + height))
    return result


# 在原图像上画矩形，框出所有人脸。
# 调用Image模块的draw方法，Image.open获取图像句柄，ImageDraw.Draw获取该图像的draw实例，然后调用该draw实例的rectangle方法画矩形(矩形的坐标即
# detectFaces返回的坐标)，outline是矩形线条颜色(B,G,R)。
# 注：原始图像如果是灰度图，则去掉outline，因为灰度图没有RGB可言。drawEyes、detectSmiles也一样。
def drawFaces(path, image_name):
    faces = detectFaces(path+image_name)
    if faces:
        img = Image.open(path+image_name)
        draw_instance = ImageDraw.Draw(img)
        for (x1, y1, x2, y2) in faces:
            draw_instance.rectangle((x1, y1, x2, y2), outline=(255, 0, 0))
        img.save(path + 'drawfaces_' + image_name)


# 保存人脸图
def saveFaces(image_name):
    faces = detectFaces(image_name)
    if faces:
        # 将人脸保存在save_dir目录下。
        # Image模块：Image.open获取图像句柄，crop剪切图像(剪切的区域就是detectFaces返回的坐标)，save保存。
        save_dir = image_name.split('.')[0] + "_faces"
        os.mkdir(save_dir)
        count = 0
        for (x1, y1, x2, y2) in faces:
            file_name = os.path.join(save_dir, str(count) + ".jpg")
            Image.open(image_name).crop((x1, y1, x2, y2)).save(file_name)
            count += 1

# 检测眼睛，返回坐标
def detectEyes(image_name):
    eye_cascade = cv2.CascadeClassifier(os.getcwd()+"\\..\\file\\haarcascade_eye.xml")
    faces = detectFaces(image_name)

    img = cv2.imread(image_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = []
    for (x1, y1, x2, y2) in faces:
        roi_gray = gray[y1:y2, x1:x2]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 2)
        for (ex, ey, ew, eh) in eyes:
            result.append((x1 + ex, y1 + ey, x1 + ex + ew, y1 + ey + eh))
    return result


# 在原图像上框出眼睛.
def drawEyes(image_name):
    eyes = detectEyes(image_name)
    if eyes:
        img = Image.open(image_name)
        draw_instance = ImageDraw.Draw(img)
        for (x1, y1, x2, y2) in eyes:
            draw_instance.rectangle((x1, y1, x2, y2), outline=(0, 0, 255))
        img.save('draweyes_' + image_name)


if __name__ == '__main__':
    time1 = datetime.now()
    result = detectFaces(os.getcwd() + "\\images\\group.jpg")
    time2 = datetime.now()
    print("耗时：" + str(time2 - time1))
    if len(result) > 0:
        print("图像有人存在，人数为：" + str(len(result)))
    else:
        print('图像中无人！！')

    drawFaces(os.getcwd() + "\\images\\", "group.jpg")
    # saveFaces(os.getcwd()+"\\images\\group.jpg")
    # drawEyes('people.jpg')
