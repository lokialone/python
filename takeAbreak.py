import webbrowser
import time

total_break = 3
break_count = 0
print("current time is" + time.ctime())
while(break_count < total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=EF-oSVCCqzU")
    break_count = break_count + 1
