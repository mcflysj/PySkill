# 使用 Python IDM 模块创建自己的下载器
# pip install internetdownloadmanager
import internetdownloadmanager as idm
def Downloader(url, output):
    pydownloader = idm.Downloader(worker=20,
                                part_size=1024*1024*10,
                                resumable=True,)

    pydownloader .download(url, output)
Downloader("Link url", "image.jpg")
Downloader("Link url", "video.mp4")