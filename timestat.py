from google_drive_downloader import GoogleDriveDownloader as gdd
import os
import math
#downloading file from the given googlr drive url
gdd.download_file_from_google_drive(file_id='1-f7EBKW43suwBTrrvaFjsFn4i70bH8Wb',dest_path='q/timestat.txt',unzip=False)
d1 = os.getcwd()
d2 = os.path.join(d1,'q')
d3 = os.path.join(d2,'timestat.txt')
#reading timestat.txt
f = open(d3,'r')
#lists of real,user and sys time
l_real = []
l_user = []
l_sys = []
i = 0
for x in f:
	i = i+1
	if i%4 == 1:
		continue
	else:
		y = x.split()
		if i%4 == 2:                                               #real times are in lines 2,6,10,.... => line number%4=2
			l_real.append(float(y[1][0]*60+y[1][2:7]))           #appending real times in the list of real times
		elif i%4 == 3:                                             #user times are in lines 3,7,11,.... => line number%4=3
			l_user.append(float(y[1][0]*60+y[1][2:7]))           #appending user times in list of user times
		elif i%4 == 0:                                             #sys times are in lines 4,8,12,.... => line number%4=0
			l_sys.append(float(y[1][0]*60+y[1][2:7]))            #appending sys times in list of sys times
def no_of_runs(l):
	return len(l)
def average(l):
	return (sum(l)/len(l))
def standard_dev(l):
	sum_sq = 0
	for x in l:
		sum_sq = sum_sq+((x-average(l))**2)                        #formula of standard deviation
	stndr_dev = math.sqrt(sum_sq/len(l))
	return stndr_dev
def get_no_of_runs_in_range(l):                                  # function to get the number of runs in range (average - standard deviation,average + standard deviation)
	upper_lim = average(l)+standard_dev(l)
	lower_lim = average(l)-standard_dev(l)
	k = 0                                                        # k is the counter of the number of runs within the range (average - standard deviation,average + standard deviation)
	for x in l:
		if x<upper_lim and x>lower_lim:
			k = k+1
	return k
print('Number of runs:',no_of_runs(l_real))
print('Average Time statistics')
print('real',average(l_real),'user',average(l_user),'sys',average(l_sys))
print('Standard deviation of Time statistics')
print('real',standard_dev(l_real),'user',standard_dev(l_user),'sys',standard_dev(l_sys))
print('Number of runs within average - standard deviation to average + standard deviation')
print('real',get_no_of_runs_in_range(l_real),'user',get_no_of_runs_in_range(l_user),'sys',get_no_of_runs_in_range(l_sys))
