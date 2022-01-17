import pyttsx3
import win32com.client
from aip import AipSpeech
from playsound import playsound

"""
pip install playsound
pip install baidu-aip
"""


def say():
    engine = pyttsx3.init()
    # 音色
    voices = engine.getProperty('voices')
    # 语速
    rate = engine.getProperty('rate')
    # 音量
    volume = engine.getProperty('volume')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.setProperty('rate', rate + 50)
        engine.setProperty('volume', volume + 1.9)
        engine.say("小柒2012真帅")
    engine.runAndWait()


def win_say():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("你好，小姐姐，能加个微信吗？")


def txt_say():
    f = open("52itstyle.txt", encoding='UTF-8')
    line = f.readline()
    engine = pyttsx3.init()
    while line:
        line = f.readline()
        print(line, end='')
        engine.say(line)
    engine.runAndWait()
    f.close()


""" 你的百度 APPID AK SK
https://console.bce.baidu.com/ai/#/ai/speech/app/list       应用列表
http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top         API
"""


def du_say():
    app_id = '253778'
    api_key = 'sYi4GIjf893Elfwjfe9pD'
    secret_key = 'rhK54Mvekwn2senIdge06Wcxzze7nmfe'
    client = AipSpeech(app_id, api_key, secret_key)
    text = "床头明月光，疑是地上霜。"
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    playsound('auido.mp3')


if __name__ == '__main__':
    du_say()


