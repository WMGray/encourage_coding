import keyboard
import os
from playsound import playsound
from path import Path
import random
import time
import threading


last_press_time = 0  # 记录上次按下的时间
cooldown_end_time = 0  # 记录冷却结束的时间
play_voice = False

sound_dir = "sounds_file"
roles = os.listdir(sound_dir)

type_1, type_2 = roles[0], roles[1]
audio_1 = [Path(sounds_files)/Path(type_1)/x for x in os.listdir(Path(sound_dir)/type_1)]
audio_2 = [Path(sounds_files)/Path(type_2)/x for x in os.listdir(Path(sound_dir)/type_2)]


def play_audio(audio_filename):
    # 播放音频的函数
    print(audio_filename)

    
def on_enter_press():
    global last_press_time, cooldown_end_time, play_voice

    current_time = time.time()
    
    if current_time < cooldown_end_time:  # 判断是否在冷却中
        return
    print("时间间隔：", current_time - last_press_time)
    print("上次摁下时间", time.asctime( time.localtime(current_time) ))
    if current_time - last_press_time < 10:
        # 时间间隔小于 10s
        threading.Timer(0, play_audio, args=[1]).start()
        time.sleep(2)
    elif 10 <= current_time - last_press_time :
        # 时间间隔在 10s- 
        threading.Timer(0, play_audio, args=[2]).start()
        time.sleep(5)

    # 更新上次按下的时间
    last_press_time = time.time()
    print("这次摁下时间", time.asctime( time.localtime(last_press_time) ))
    print()
    
"""keyboard.add_hotkey("enter", on_enter_press)
keyboard.wait()  # 一直等待键盘事件的发生"""
print(audio_1)