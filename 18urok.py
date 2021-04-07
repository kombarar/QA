sec = int(input())
minutes = int(input())
hour = int(input())

def perevod(sec,minutes,hour):
    alltime = sec
    alltime = alltime + (minutes*60)+(hour*3600)
    print(alltime)
perevod(sec,minutes,hour)