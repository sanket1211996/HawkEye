
import subprocess
import math
import datetime
import re


# def get_video_duration():
#     result = subprocess.Popen(["ffprobe", "D:\\Project\\HawkEye\\video\\13.3.2018.12.0.40.avi"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     matches = [x for x in result.stdout.readlines() if "Duration" in x]
#     duration_string = re.findall(r'Duration: ([0-9:]*)', matches[0])[0]
#     return math.ceil(duration_string_to_timedelta(duration_string).seconds)
#
# def duration_string_to_timedelta(s):
#     [hours, minutes, seconds] = map(int, s.split(':'))
#     seconds = seconds + minutes * 60 + hours * 3600
#     return datetime.timedelta(seconds=seconds)
#
