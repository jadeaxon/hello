#!/usr/bin/env python3

# Code to help with swim club administration.
import glob
import os
import statistics
from pathlib import Path

SWIM_DATA_DIR = 'data' # swim data subdir

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
    file = file.removeprefix(f'{SWIM_DATA_DIR}\\')
    r = parse_filename(file)
    (name, age, distance, stroke) = r
    # print(r)
    # print(lines[0], end="")
    times = lines[0].strip().split(',')
    str_times = times.copy()
    times = list(map(time_to_hundredths, times))
    # print(times)
    average = sum(times) / len(times) # in hundredths
    average = statistics.mean(times) # same thing
    average = int(round(average, 0))
    # print(average)
    str_average = hundredths_to_time(average)
    # print(t)
    # print()
    return (name, age, distance, stroke, str_times, str_average)

def main():
    print(os.getcwd())
    files = os.listdir(SWIM_DATA_DIR) # almost the same thing as below
    files = glob.glob(f'{SWIM_DATA_DIR}/*.txt')

    for file in files:
        path = Path(file) # to get the file basename
        print(f"Processing {path.name}...")
        swim_data = read_swim_data(file)
        print(swim_data)

if __name__ == '__main__':
    main()
    
