# Code to help with swim club administration.
import glob
import os
import statistics

def parse_filename(filename):
    L = filename.removesuffix(".txt").split('-')
    name, age, distance, stroke = L
    age = int(age)
    stroke = stroke.lower()
    return (name, age, distance, stroke)

def time_to_hundredths(time):
    if ':' in time:
        minutes, time = time.split(':')
    else:
        minutes = 0
    seconds, hundredths = time.split(".")
    minutes = int(minutes)
    seconds = int(seconds)
    hundredths = int(hundredths)
    seconds += minutes * 60
    hundredths += seconds * 100
    return hundredths

def hundredths_to_time(h):
    minutes = h // (60 * 100)
    h = h % (60 * 100)
    seconds = h // 100
    h = h % 100
    hundredths = h
    if minutes > 0:
        r = f"{minutes}:{seconds:02d}.{hundredths}"
    else:
        r = f"{seconds:02d}.{hundredths}"
    return r

def read_swim_data(file):
    with open(file) as f:
        lines = f.readlines() 
    file = file.removeprefix('data\\')
    r = parse_filename(file)
    print(r)
    print(lines[0], end="")
    times = lines[0].strip().split(',')
    times = list(map(time_to_hundredths, times))
    print(times)
    average = sum(times) / len(times) # in hundredths
    average = statistics.mean(times) # same thing
    average = int(round(average, 0))
    print(average)
    t = hundredths_to_time(average)
    print(t)
    print()

print(os.getcwd())
files = glob.glob('data/*.txt')
for file in files:
    read_swim_data(file)
    
