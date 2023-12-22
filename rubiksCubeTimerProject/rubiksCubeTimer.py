from dataclasses import dataclass
from designer import *
import time
import winsound

@dataclass
class World:
    timer: DesignerObject
    first_timer: bool
    second_timer: bool
    timer_started: bool
    start_time: float
    live_timer: float
    
def start_game(world:World, key:str):
    if key == "space":
        world.start_time = time.time()
        world.first_timer = True
        world.timer_started = True

def end_game(world:World, key:str):
    if world.timer_started and key != 'space':
        world.timer_started = False
    
def start_initial_timer(world:World):
    if world.first_timer:
        live_time = time.time()
        world.live_timer = live_time - world.start_time
        world.live_timer = 15 - round(world.live_timer,2)
        if world.live_timer <= -0.01:
            world.first_timer = False
            world.second_timer = True
            world.start_time = time.time()
            winsound.Beep(1000, 1000)
            
def update_timer(world:World):
    world.timer.text = str(world.live_timer)[:4]

def start_second_timer(world:World):
    if world.second_timer and world.timer_started:
        live_time = time.time()
        world.live_timer = live_time - world.start_time
        
def create_world():
    return World(text("white","null", 100,get_width()/2,150),False,False,False,0.0,0.0)

background_image("uziVsTheWorld.jpg")
when('starting', create_world)
when('typing',start_game)
when('typing', end_game)
when('updating',start_initial_timer)
when('updating',start_second_timer)
when('updating',update_timer)
start()