import numpy as np
import re
import io
from scipy.interpolate import interp1d

# Interpolates starting times of verses based on a subset of times
def interpolate_times(time_stamps):
    keys = sorted(list(time_stamps.keys()))
    values = [time_stamps[k] for k in keys]
    
    f = interp1d(keys, values)
    
    x = np.arange(1,keys[-1]+1)
    return f(x)


# Loads from a file a poem (runo) of Kalevala as a list of strings (verses).
def load_text(runo, version="fi"):
    assert(runo > 0 and runo < 51)
    assert(version in ["fi", "en_kirby"])
    runot = []
    if version == "fi":
        with io.open("kalevala_fi.txt", 'r', encoding='utf8') as fp:
            first_reached = False
            empty_count = 0
            lines = []
            for line in fp:
                if line.startswith("Ensimmäinen runo"):
                    first_reached = True
                    continue
                if not first_reached:
                    continue
                if line.isspace():
                    if len(lines)>1 and empty_count>1:
                        runot.append(lines)
                        lines = []
                        empty_count = 0
                    elif len(lines)==1: # Skip the runo title
                        lines = []
                    empty_count+=1
                    continue
                if line == "* * *\n":
                    continue
                
                lines.append(line.strip())
    
    elif version == "en_kirby":
        assert(runo > 0 and runo < 26)
        with io.open("kalevala_en_kirby_1907.txt", 'r', encoding='utf8') as fp:
            first_reached = False
            empty_count = 0
            lines = []
            for line in fp:
                if line.startswith("RUNO I."):
                    first_reached = True
                    continue
                if not first_reached:
                    continue
                if line.isspace():
                    continue
                if not line.startswith(" "):
                    if len(lines) > 0:
                        runot.append(lines)
                        lines = []
                    continue
                lines.append(re.split(r'\s{2,}', line.strip())[0])

    return runot[runo-1]


# Converts seconds to string hh:MM:ss,mmm
def seconds_to_time(seconds):
    ms = int(round((seconds - int(seconds))*1000))
    seconds = int(seconds)
    h = seconds//3600
    seconds -= 3600*h
    m = seconds//60
    s = seconds - 60*m
    return "{:0>2}:{:0>2}:{:0>2},{:0>3}".format(h, m, s, ms)


# Prints the subtitles in .srt format to a file. 
def print_srt(text, times, file_path, test=False):
    assert(len(text) == len(times)-1)
    with io.open(file_path, 'w', encoding='utf8') as f:
        for i, t in enumerate(text):
            print(i+1, file=f)
            print(seconds_to_time(times[i]) + " --> " + seconds_to_time(times[i+1]), file=f)
            if test: print(i+1, end=" ", file=f)
            print(t, file=f)
            print(file=f)


# Repeats the two last lines of a poem
def add_repeat(text):
    return text + [text[-2], text[-1]]


# Converts minutes and seconds to seconds
time = lambda m,s: 60*m+s


# Generates subtitles for poem 1
def runo_1(test=False):
    text_fi = load_text(1, "fi")
    text_en = load_text(1, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,13),
                    25:     time(1,44),
                    50:     time(3,15),
                    75:     time(4,44),
                    100:    time(6,10),
                    125:    time(7,35),
                    150:    time(8,58),
                    175:    time(10,20),
                    200:    time(11,42),
                    225:    time(13,3),
                    250:    time(14,24),
                    275:    time(15,45),
                    300:    time(17,5),
                    325:    time(18,25),
                    345:    time(19,30),
                    346:    time(19,33),
                    347:    time(19,37)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_1_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_1_en.srt", test=test)


# Generates subtitles for poem 3
def runo_3(test=False):
    text_fi = load_text(3, "fi")
    text_en = load_text(3, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,14),
                    25:     time(1,42),
                    50:     time(3,10),
                    75:     time(4,37),
                    100:    time(6,3),
                    125:    time(7,26),
                    150:    time(8,50),
                    175:    time(10,11),
                    200:    time(11,32),
                    225:    time(12,52),
                    250:    time(14,10),
                    275:    time(15,29),
                    300:    time(16,46),
                    325:    time(18,3),
                    350:    time(19,20),
                    375:    time(20,36),
                    400:    time(21,52),
                    425:    time(23,7),
                    450:    time(24,22),
                    475:    time(25,37),
                    500:    time(26,52),
                    525:    time(28,6),
                    550:    time(29,20),
                    581:    time(30,52),
                    582:    time(30,55),
                    583:    time(30,59)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_3_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_3_en.srt", test=test)
