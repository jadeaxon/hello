#!/usr/bin/env python3

# Using .env file instead.
# It only gets you code completion. IDE not picking it up for import.
# Brute force it.
import sys
sys.path.append(r'C:\Users\jadea\projects\pythonplus')

# Code to help with swim club administration.
import glob
import os
import statistics
from pathlib import Path
from pythonplus import StringInteger
from textwrap import dedent

SWIM_DATA_DIR = 'data' # swim data subdir
time_si = StringInteger(
    "0123456789", ":", 
    "012345", "0123456789", ".",
    "0123456789", "0123456789")
time_si.leading_zeros = False
time_si.zero_pad = 4

def parse_filename(filename):
    L = filename.removesuffix(".txt").split('-')
    name, age, distance, stroke = L
    age = int(age)
    stroke = stroke.lower()
    return (name, age, distance, stroke)

def time_to_hundredths(time):
    global time_si
    time_si.set(time)
    hundredths = time_si.int()
    return hundredths 

def time_to_hundredths_old(time):
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
    time_si.set(h)
    return time_si.str()

def hundredths_to_time_old(h):
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

def create_bar_chart_html(record):
    (swimmer, age, distance, stroke, times, average) = record
        
    chart_html = ""
    max_time_int = 0
    for t in times:
        time_si.set(t)
        t_int = time_si.int()
        if t_int > max_time_int: max_time_int = t_int

    for i, t in enumerate(reversed(times)):
        time_si.set(t)
        t_int = time_si.int()
        chart_html += create_bar_chart_svg(t_int, max_time_int, len(times) - i)

    title = f"{swimmer} (age {age}) {distance} {stroke}"
    print(title)
    
    # Match indent level.
    # No way to do this via format spec.
    # You have to use full value, not value after dedent.
    chart_html = chart_html.replace("\n", "\n" + " " * 8)
    
    html = dedent(f"""
    <!DOCTYPE html>
    <html>
      <head>
        <title>{title}</title>
      </head>
      <body>
        <h3>{title}</h3>
        {chart_html}
      </body>
    </html>
    """)
    return html

def create_bar_chart_svg(time_int, max_time_int, i):
    percent = time_int / max_time_int
    max_width = 400
    width = int(max_width * percent)

    html = dedent(f"""
    <svg height="30" width="400">
      <rect height="30" width="{width}" style="fill:rgb(0,0,255);" />
    </svg>Label {i}<br />              
    """)
    return html

def main():
    print(os.getcwd())
    files = os.listdir(SWIM_DATA_DIR) # almost the same thing as below
    files = glob.glob(f'{SWIM_DATA_DIR}/*.txt')
    records = []
    charts = []

    for i, file in enumerate(files, start=1):
        path = Path(file) # to get the file basename
        print(f"Processing file {i}: {path.name}...")
        swim_data = read_swim_data(file)
        records.append(swim_data)
        print(swim_data)
    print(f"Processed {i} files.")

    for record in records:
        html = create_bar_chart_html(record)
        print(html)
        charts.append(html)

    # print(charts)
if __name__ == '__main__':
    main()
    
