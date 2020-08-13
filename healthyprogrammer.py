from pygame import mixer 
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while(1):
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
        
def log_now(msg):
    with open("harshit.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
        
if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    eyesecs = 20
    exsecs = 10
    
    while True:
        if time() - init_water > watersecs:
            print("water drinking time. Enter 'drank' to stop the alarm ")
            musiconloop('water.mp3','drank')
            init_water= time()
            log_now("drank water at") 
    
        if time() - init_eyes > eyesecs:
            print("Eyes exerise time. Enter 'doneeyes' to stop the alarm")
            musiconloop('water.mp3','doneeyes')
            init_eyes= time()
            log_now("eyes exercise at") 
            
        if time() - init_exercise > exsecs:
            print("Exercise time. Enter 'doneexercise' to stop the alarm")
            musiconloop('water.mp3','doneexercise')
            init_exercise= time()
            log_now("exercise done at") 