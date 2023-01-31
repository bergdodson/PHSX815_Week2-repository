#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import time
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append("C:\\Users\\bergd\\Desktop\\github\\HW 4") # For running in the IDE console
sys.path.append('/mnt/c/Users/bergd/Desktop/github/HW 4') # For running in the Ubuntu terminal
from python.MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    # Boolean telling us to resolve command line flags if there are any
    # Or continue if there aren't any flags. Initializing it here at the
    # beginning of the script
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()
    
    #start = time.time() #Used to measure how long these sorting methods took
    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times)
    # times_avg = Sorter.InsertionSort(times)
    # times_avg = Sorter.QuickSort(times)
    #end = time.time()
    
    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    
    # Seeing if the sorting worked, what the average value was, and how long everything took.
    #print(times)
    #print
    #print(times_avg)
    #print(end-start)
    
    #Calculating Quartiles
    ntimes = len(times)
    medianindex = ntimes/2
    
    #Finding the median,1st, and 3rd quartiles
    if medianindex % 1 == 0:
        median = (times[int(medianindex - 1)] + times[int(medianindex - 1)])/2
        
        # Getting Quartiles
        quartindex = medianindex/2
        
        if quartindex % 1 == 0:
            firstq = (times[int(medianindex - quartindex)] + times[int(medianindex - quartindex - 1)])/2
            thirdq = (times[int(medianindex + quartindex)] + times[int(medianindex + quartindex - 1)])/2
            
        else:
            firstq = times[int(medianindex - quartindex - 0.5)]
            thirdq = times[int(medianindex + quartindex - 0.5)]
        
    else:
        median = times[int(medianindex - 0.5)]
        spacer = medianindex - 0.5
        
        #Getting Quartiles
        quartindex = spacer / 2
        
        if quartindex % 1 == 0:
            firstq = (times[int(spacer - quartindex - 1)] + times[int(spacer - quartindex)]) / 2
            thirdq = (times[int(spacer + quartindex - 1)] + times[int(spacer + quartindex)]) / 2
            
        else:
            firstq = times[int(spacer - quartindex - 0.5)] 
            thirdq = times[int(spacer + quartindex - 0.5)]
        
    # 1st and 3rd quartile

    #Plotting directives
    title = 'Time between cookies disappearing'
    
    n, bins, patches = plt.hist(times, 50, density=True, facecolor='g', alpha=0.75)
    plt.xlabel('Time (days)')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)
    plt.axvline(times_avg, color = 'k', linestyle = 'dashed', linewidth = 1)
    plt.text(t_avg + 0.025, 0.6, 'Mean',rotation = 'vertical' )
    plt.axvline(median, color = 'r', linestyle = 'dashed', linewidth = 1)
    plt.text(median - 0.25, 0.6, 'Median',rotation = 'vertical' )
    plt.axvline(firstq, color = 'b', linestyle = 'dashed', linewidth = 1)
    plt.text(firstq - 0.25, 0.6, '1st Quartile',rotation = 'vertical' )
    plt.axvline(thirdq, color = 'b', linestyle = 'dashed', linewidth = 1)
    plt.text(thirdq + 0.1, 0.6, '3rd Quartile',rotation = 'vertical')
    plt.savefig('randomnums_rate 1_numexp 10000_fig1.tif')
    plt.show()