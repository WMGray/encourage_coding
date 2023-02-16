import keyboard
import os
from playsound import playsound
from path import Path
import random
import time

last_press_time = 0  # 记录上次按下的时间
cooldown_end_time = 0  # 记录冷却结束的时间

sound_dir = "sounds_file"
roles = [Path(sound_dir)/x for x in os.listdir(sound_dir)]
print(roles)
type_1, type_2 = os.listdir(roles[0])
audio_1 = [Path(roles[0])/Path(type_1)/x
           for x in os.listdir(Path(roles[0])/type_1)]
audio_2 = [Path(roles[0])/Path(type_2)/x
           for x in os.listdir(Path(roles[0])/type_2)]


def play_audio(audio_filename, sleep_time: int):
    # 播放音频的函数
    playsound(audio_filename)
    time.sleep(sleep_time)

    
def on_enter_press():
    global last_press_time, cooldown_end_time, play_voice

    current_time = time.time()
    
    if current_time < cooldown_end_time:  # 判断是否在冷却中
        return

    if current_time - last_press_time < 10:
        # 时间间隔小于 10s
        play_audio(random.choice(audio_1), 2)
    elif 10 <= current_time - last_press_time:
        # 时间间隔在 10s- 
        play_audio(random.choice(audio_2), 3)

    # 更新上次按下的时间
    last_press_time = time.time()


keyboard.add_hotkey("enter", on_enter_press)
keyboard.wait()  # 一直等待键盘事件的发生