import exifread


def read():
    GPS = {}
    date = ''
    with open("D:\py项目工程\自动化测试\练习\IMG20201013135058.jpg", 'rb') as f:
        contents = exifread.process_file(f)
        print(contents)
        for key in contents:
            if key == "GPS GPSLongitude":
                print("经度 =", contents[key], contents['GPS GPSLatitudeRef'])
            elif key == "GPS GPSLatitude":
                print("纬度 =", contents[key], contents['GPS GPSLongitudeRef'])


if __name__ == '__main__':
    read()


def process_img(path):
    """
    这个函数用来处理图片 并返回图片的 经纬度、拍摄时间信息
    :return: 返回图片信息 是一个字典
    """
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    info = {
        # 注意 这里获得到的是值 需要使用 values方法
        'Image DateTime(拍摄时间)': tags.get('Image DateTime', '0').values,
        'GPS GPSLatitudeRef(纬度标志)': tags.get('GPS GPSLatitudeRef', '0').values,
        'GPS GPSLatitude(纬度)': tags.get('GPS GPSLatitude', '0').values,
        'GPS GPSLongitudeRef(经度标志)': tags.get('GPS GPSLongitudeRef', '0').values,
        'GPS GPSLongitude(经度)': tags.get('GPS GPSLongitude', '0').values
    }
    return info


def process_num(x):
    """
    处理经纬度 将其转化为 xx.xxxxxx格式
    注意列表中的每一个元素 是 <class 'exifread.utils.Ratio'>
    由于最后一个是 10243/2000 这样的格式 需要手动将其处理 其余的使用 .num 方法就能获得到值
    :param x: 传入的经度和纬度
    :return: 处理好了经纬度
    """
    # 处理列表中最后一个元素
    x_last = eval(str(x[-1]))
    #  转化
    new_x = x[0].num + x[1].num / 60 + x_last / 3600

    return '{:.13f}'.format(new_x)


def main():
    img_path = r'./1.jpg'
    info_dict = process_img(img_path)
    lat = info_dict.get('GPS GPSLatitude(纬度)')
    lng = info_dict.get('GPS GPSLongitude(经度)')

    print('拍摄时间: {}，GPS位置:纬度{}{},经度{}{}'.format(info_dict.get('Image DateTime(拍摄时间)'),
                                                info_dict.get('GPS GPSLatitudeRef(纬度标志)'),
                                                process_num(lat),
                                                info_dict.get('GPS GPSLongitudeRef(经度标志)'),
                                                process_num(lng),
                                                ))
