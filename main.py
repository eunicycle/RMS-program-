# Program was created by Neftali Eunice Romero and Cavanaugh Carter
# This program calculates the root mean square of the BLUED data
# this 0
# veriabes :
#     Ia1 or Ia2 = current from main A
#     Ib1 or Ib2 = current from Main B
#     counterA   = counter for main A
#     counterB   = counter for the main B
#     TimestampA = time stamp of the polarity change in main B
#     TimestampB = time stamp for the polarity change in main B
#     inputfile = input file name
#     header    = header of file
#     flag      = flag to exit loop
#
# INPUT : filename,
# OUTPUT : outputfile should be defned by user specifying file which will be
#          filled with rms values. *** copy inputfile add decriptor for output of rms.
#------------------------
# open input
import math
# this is the rms function that is called in the for loop
def rms(x,counter):
    total = math.sqrt(float(x)/float(counter))
    #print x, counter
    return total

# end of rms FUNCTION
while (True):
    try:
        inputfile = open( input("Please insert input filename:"), 'r')
        print(inputfile)
        break
    except IOError:
        print ('File input invalid')
        pass

# read header lines
flag =1
x=0
while (flag==1) :# checking header
    x=x+1
    header=inputfile.readline(3)
    if (header=="X_V"):
        flag=2
        #header = inputfile.readline()
        #print header
    else:
        headerlines=inputfile.readline()
        #print header
# manually open outputfile
outputfileA = open(input("Please insert inputfilename and 'A' for main A:"), "w")
outputfileB = open(input("Please insert inputfilename and 'B' for main B:"),"w")
#Split the readline for Timestamp and IA1 and IB1
counterA= 0
counterBB = 0
sumsqA = 0
sumsqB = 0
Ia2 = 0
Ib1 = 0
Ia1 = 0
Ib2 = 0
inputfile.readline()
for line in inputfile:
    Ia2 =Ia1
    Ib2 = Ib1
    Timestamp,Ia1,Ib1, Va = line.split(',',3)

    if (float(Ia1) > 0 and float(Ia2) < 0):# only send variables x and counter to the function for ful cycle
        #print sumsqA, counterA
        result = rms(sumsqA, counterA)#function
        outputfileA.write('%s, %3.3f\n' % (Timestamp, result))# writing to an output file using 4 sigfigs to report
        counterA=0 # re initialize the counter
        sumsqA =0
        #print ('I am here')
    else: # does the sum of squares for the rms function
        counterA = counterA + 1
        sumsqA = float(Ia1)**2 + sumsqA
    if (float(Ib1) > 0 and float(Ib2) < 0):
        result = rms(sumsqB, counterBB)
        outputfileB.write('%s, %3.3f\n' % (Timestamp, result))
        counterBB = 0
        sumsqB = 0
    else:
        counterBB = counterBB + 1
        sumsqB = sumsqB + float(Ib1)**2


outputfileA.close
outputfileB.close
inputfile.close
