# For my exercises, set a timer that tells me when to start and stop each
# exercise.

import time
import subprocess
import webbrowser

def run_exercise_program(voice):
    """Kaiser Personal exercise program - Assigned 2016-05-17"""
    speak(voice, 'Exercise program starting')
    # The White Stripes - Death Letter Live
    # webbrowser.open_new('http://www.infinitelooper.com/?v=AaCTxcnfB6Y&p=n')
    time.sleep(15)
    for i in range(2):
        run_exercise(20, 5, 2, voice)
        time.sleep(15)
    time.sleep(15)
    run_exercise(3, 20, 10, voice)
    time.sleep(30)
    for i in range(2):
        run_exercise(4, 10, 10, voice)
        time.sleep(10)
    run_exercise(20, 1, 1, voice)
    time.sleep(15)
    run_exercise(3, 20, 10, voice)
    speak(voice, 'Exercise program completed')
    return True

def run_exercise(number_of_reps, exercise_time, break_time, voice):
    print 'New exercise started...'
    speak(voice, 'New exercise started')
    for index in range(1, number_of_reps + 1):
        print index
        speak(voice, index)
        speak(voice, 'start')
        time.sleep(exercise_time)
        speak(voice, 'stop')
        if index != number_of_reps:
            time.sleep(break_time)
    speak(voice, 'Exercise completed')
    return True

def speak(voice, phrase):
    # say call
    command = 'say -v {0} {1}'.format(voice, phrase)
    command_list = command.split(' ')
    return subprocess.call(command_list)

if __name__ == '__main__':
    voice = 'Samantha'
    run_exercise_program(voice) 
