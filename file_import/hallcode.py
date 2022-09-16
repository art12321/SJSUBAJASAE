import time
import board
import digitalio

STATE_HIGH       = 0
STATE_LOW        = 1
s_states = ['STATE_HIGH','STATE_LOW']

EVENT_NONE   = 0
EVENT_FLIP   = 1

hall = digitalio.DigitalInOut(board.A0)
hall.direction = digitalio.Direction.INPUT

def hall_event():
    global hall_prev
#    hall_prev = None

    hall_curr = hall.value
    
    if ((hall_curr == False) and (hall_prev == True)):
        ret = EVENT_FLIP
    elif ((hall_curr == True) and (hall_prev == False)):
        ret = EVENT_FLIP
    else:
        ret = EVENT_NONE

    hall_prev = hall_curr
    return ret

def event_process(s, e):
    if s == STATE_HIGH:
        if e == EVENT_FLIP:
            return STATE_LOW
    elif s == STATE_LOW:
        if e == EVENT_FLIP:
            return STATE_HIGH

state = STATE_HIGH
hall_prev = hall.value

while True:
    event = hall_event()
    if event != EVENT_NONE:
        state_new = event_process(state, event)
        if (state_new != state):
            print("flip")
        state = state_new