"""
    破解zip压缩文件
"""
import optparse
import zipfile
from threading import Thread
from tqdm import tqdm


def extract_file(zip_file, password):
    """ 提取压缩文件，通过密码不断尝试 """
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        print(f'\n  发现密码，正确密码为：{password}')
    except:
        pass


def main():
    """ 通过optparse模块进行py命令行形式脚本操作，获取字典和zip路径 """
    parser = optparse.OptionParser('\n  %prog -z <zipfile> -d <dictionary>')
    parser.add_option('-z', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    options, args = parser.parse_args()
    if options.zname and options.dname:
        zip_name = options.zname
        dict_name = options.dname
    else:
        print(parser.usage)
        exit(0)

    """
    zip_name 为待破解的压缩文件全路径字符串
    dict_name 为密码破解字典文件全路径字符串
    """
    try:
        zip_file = zipfile.ZipFile(zip_name)
        with open(dict_name, 'r', encoding='utf-8') as f:
            for line in tqdm(f.readlines()):
                password = line.strip('\n')
                thread = Thread(target=extract_file, args=(zip_file, password))
                thread.start()
    except Exception as e:
        print(f'发生异常！请检查文件是否存在！异常信息为：{e}')


main()
