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

    time_stamps = { 1:      time(0,12.6),
                    25:     time(1,44.2),
                    50:     time(3,15.5),
                    75:     time(4,44.5),
                    100:    time(6,10.6),
                    125:    time(7,35.2),
                    150:    time(8,58.5),
                    175:    time(10,20.6),
                    200:    time(11,42.6),
                    225:    time(13,3.7),
                    250:    time(14,24.3),
                    275:    time(15,45.1),
                    300:    time(17,5.4),
                    325:    time(18,25.7),
                    345:    time(19,30),
                    346:    time(19,33),
                    347:    time(19,37)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_01_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_01_en.srt", test=test)


# Generates subtitles for poem 2
def runo_2(test=False):
    text_fi = load_text(2, "fi")
    text_en = load_text(2, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,14.6),
                    25:     time(1,53.6),
                    50:     time(3,29.7),
                    75:     time(5,2),
                    100:    time(6,31),
                    125:    time(7,58.6),
                    150:    time(9,25.4),
                    175:    time(10,50.2),
                    200:    time(12,13.5),
                    225:    time(13,36.9),
                    250:    time(14,59.7),
                    275:    time(16,22.5),
                    300:    time(17,44.6),
                    325:    time(19,5.4),
                    350:    time(20,26.2),
                    379:    time(22,0.1),
                    380:    time(22,3.6),
                    381:    time(22,8)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_02_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_02_en.srt", test=test)


# Generates subtitles for poem 3
def runo_3(test=False):
    text_fi = load_text(3, "fi")
    text_en = load_text(3, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,14.9),
                    25:     time(1,42.2),
                    50:     time(3,10.5),
                    75:     time(4,37.3),
                    100:    time(6,2.8),
                    125:    time(7,26.4),
                    150:    time(8,49.8),
                    175:    time(10,11.6),
                    200:    time(11,32.4),
                    225:    time(12,52.2),
                    250:    time(14,10.8),
                    275:    time(15,29.2),
                    300:    time(16,46),
                    325:    time(18,3.6),
                    350:    time(19,20.1),
                    375:    time(20,36.2),
                    400:    time(21,52.1),
                    425:    time(23,7.4),
                    450:    time(24,22.5),
                    475:    time(25,37.3),
                    500:    time(26,52),
                    525:    time(28,6.3),
                    550:    time(29,20.3),
                    581:    time(30,51.9),
                    582:    time(30,55.2),
                    583:    time(30,59)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_03_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_03_en.srt", test=test)


    # Generates subtitles for poem 4
def runo_4(test=False):
    text_fi = load_text(4, "fi")
    text_en = load_text(4, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,38.9),
                    25:     time(2,15.1),
                    50:     time(3,53.4),
                    75:     time(5,29.2),
                    100:    time(7,3),
                    125:    time(8,35.3),
                    150:    time(10,6.1),
                    175:    time(11,35.6),
                    200:    time(13,4),
                    225:    time(14,31.2),
                    250:    time(15,57.5),
                    275:    time(17,23.1),
                    300:    time(18,48.2),
                    325:    time(20,12.5),
                    337:    time(20,54),
                    350:    time(21,39.7),
                    372:    time(22,56.4),
                    373:    time(23,07.5),
                    375:    time(23,14.6),
                    400:    time(24,41),
                    425:    time(26,5),
                    450:    time(27,28.3),
                    475:    time(28,51.6),
                    500:    time(30,15.2),
                    519:    time(31,19.3),
                    520:    time(31,23.1),
                    521:    time(31,28)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_04_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_04_en.srt", test=test)
    
    
# Generates subtitles for poem 5
def runo_5(test=False):
    text_fi = load_text(5, "fi")
    text_en = load_text(5, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,30.9),
                    25:     time(1,57.9),
                    50:     time(3,26.2),
                    75:     time(4,52.5),
                    100:    time(6,17.6),
                    125:    time(7,43.1),
                    133:    time(8,10.3),
                    134:    time(8,17.3),
                    150:    time(9,12.2),
                    175:    time(10,36.7),
                    200:    time(12,1.5),
                    225:    time(13,26.6),
                    242:    time(14,24.5),
                    243:    time(14,28),
                    244:    time(14,33)}
                    
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_05_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_05_en.srt", test=test)
    

# Generates subtitles for poem 6
def runo_6(test=False):
    text_fi = load_text(6, "fi")
    text_en = load_text(6, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,17.3),
                    25:     time(1,48.7),
                    50:     time(3,24.5),
                    75:     time(4,59.8),
                    100:    time(6,33.3),
                    125:    time(8,7.1),
                    150:    time(9,41.3),
                    175:    time(11,14.8),
                    200:    time(12,48.5),
                    225:    time(14,21.9),
                    235:    time(14,59.3),
                    236:    time(15,3.6),
                    237:    time(15,9)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_06_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_06_en.srt", test=test)


# Generates subtitles for poem 7
def runo_7(test=False):
    text_fi = load_text(7, "fi")
    text_en = load_text(7, "en_kirby")

    text_fi = add_repeat(text_fi)
    text_en = add_repeat(text_en)

    assert(len(text_fi) == len(text_en))

    time_stamps = { 1:      time(0,32.5),
                    25:     time(1,58.3),
                    50:     time(3,25.7),
                    75:     time(4,52.3),
                    100:    time(6,18.1),
                    125:    time(7,43.4),
                    150:    time(9,8.7),
                    175:    time(10,33.2),
                    200:    time(11,57.8),
                    225:    time(13,22.9),
                    250:    time(14,48.2),
                    275:    time(16,12.5),
                    300:    time(17,36.6),
                    325:    time(19,0.4),
                    350:    time(20,23.5),
                    369:    time(21,27.1),
                    370:    time(21,30.6),
                    371:    time(21,35)}
    times = interpolate_times(time_stamps)

    print_srt(text_fi, times, "subtitles/runo_07_fi.srt", test=test)
    print_srt(text_en, times, "subtitles/runo_07_en.srt", test=test)