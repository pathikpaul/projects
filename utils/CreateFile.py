import random
import time
sizedict={'K':1024, 'M':1024*1024, 'G':1024*1024*1024, 'T':1024*1024*1024*1024}
FileFolder="files-"
for size_types in 'K' 'M' 'G' 'T' :
    for inputsize in [1,10,100]:
        FileName=FileFolder+str(inputsize)+size_types
        t0=time.time()
        with open(FileName, "wt") as f:
            for x in range(0, int(inputsize*sizedict[size_types]/10)):
                f.write('{0:2d},{1:6d}'.format(random.randint(1,59),random.randint(1,999999)))
                f.write("\n")
            f.close()
        t1=time.time()
        print('Command tool {0} seconds'.format(t1-t0),FileName)

