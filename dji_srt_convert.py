import datetime
import sys

infile = open(sys.argv[1], "rt")
outfile = open(sys.argv[2], "wt")
ar43or169 = str(sys.argv[3])

for line in infile:
    
    s = line
    if s[0] == "s":
        words = s.split()
        signal = words[0].replace("signal:", "")
        ch = words[1].replace("ch:", "CH")
        flightTime = words[2].replace("flightTime:", "")
        uavBat = words[3].replace("uavBat:", "")
        glsBat = words[4].replace("glsBat:", "")
        uavBatCells = words[5].replace("uavBatCells:", "uavBatCells:")
        glsBatCells = words[6].replace("glsBatCells:", "glsBatCells:")
        delay = words[7].replace("delay:", "")
        bitrate = words[8].replace("bitrate:", "")
        timeF = str(datetime.timedelta(seconds=int(flightTime)))
        
        #16:9
        if ar43or169 == "169":
            outfile.write("\t                                                                 " + delay + "  " + bitrate + "\n\t" + signal + " " + ch + "                                                      " + uavBat + " " + timeF[2:] + " " + glsBat + "\n")
        #4:3
        if ar43or169 == "43":
            outfile.write("\t                                             " + delay + "  " + bitrate + "\n\t" + signal + " " + ch + "                                  " + uavBat + " " + timeF[2:] + " " + glsBat + "\n")
    else:
        outfile.write(line)
    
infile.close()
outfile.close()

print("DONE!")
