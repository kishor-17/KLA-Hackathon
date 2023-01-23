from datetime import datetime
import math

f = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 1\Format_Source.txt", "r")


current_time = datetime.now()
  
time_stamp = current_time.timestamp()
date_time = datetime.fromtimestamp(time_stamp)
str_date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")

start="header 600 \nbgnlib "+str_date_time+" "+str_date_time+"\nlibname egdslib\nunits 0.0001 1e-10\n\nbgnstr "+str_date_time+" "+str_date_time+"\nstrname top\n\n"
end="endstr\nendlib"
#Milestone 1

def Milestone1():
    inp=f.readlines()[8:13]
    print(inp)
    data=""
    for i in inp:
        data+=i

    out=start+data+end
    print(out)

    fc = open('output.txt', 'w')
    fc.write(start+data+end)

#Milestone 1 completed

def Parse_data(fm2_s):            #used for parsing datas in source file
    st=fm2_s.readlines()[8:]      #['boundary\n', 'layer 1\n', 'datatype 0\n', 'xy  7  -180 43010  -180 47850  1190 47850  1190 44280  3630 44280  3630 43010  -180 43010\n', 'endel\n']
    st=st[:len(st)-2]
    data=[]
    #print(st)
    i=0
    while i <len(st):
        data.append(st[i:i+5])
        i+=5
    #print(data[0])
    return data

def distance_vector(v):     #TO FIND DISTANCE BETWEEN 2 POINTS   -  RETURNS DISTANCE
    dist=[]
    for i in range(len(v)):
        s=[]
        for j in range(len(v[i])-1):
            s.append(math.dist(v[i][j],v[i][j+1]))
        dist.append(s)
    return dist


def output_format(inp):    #ADD OUTPUT TO THE STRING FOR WRITING IN FILE
    data=""
    for i in inp:
        data+=i
    return data


def Parse_coord(data):       #PARSE THE COORDINATES FROM LIST
    POI_coord = []
    for i in data:
        spt = i[3].split("  ")
        points1 = ''
        if int(spt[1])>=10:
            points1=i[3][8:]
        else:
            points1 = i[3][7:]
        #print(points1)
        coord=points1.split("  ")
        #print(coord)
        co=[]
        for i in coord:
            s=i.split(" ")
            cod = []
            #print(s)
            cod.append(int(s[0]))
            cod.append(int(s[1]))
            co.append(cod)
        #print(co)
        POI_coord.append(co)
    return POI_coord


def Milestone2():
    fm2_s= open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 2\Source.txt", "r")
    data_s = Parse_data(fm2_s)
    Src_coord = Parse_coord(data_s)


    fm2_POI = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 2\POI.txt", "r")
    data_POI = Parse_data(fm2_POI)
    POI_coord = Parse_coord(data_POI)

    Src_dist=distance_vector(Src_coord)
    POI_dist=distance_vector(POI_coord)


    fc = open('output2.txt', 'w')
    out=""
    for i in range(len(POI_dist)):     #check for distance
        for j in range(len(Src_dist)):
            ratio=POI_dist[i][0]/Src_dist[j][0]       #RATIO 
            flag=0
            for k in range(len(Src_dist[0])):
                if POI_dist[i][k]/Src_dist[j][k]!=ratio:
                    flag=1
                    break
            if flag==0:
                out+=output_format(data_s[j])
    fc.write(out)
    print(out)


def Milestone3():
    fm3_s= open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 3\Source.txt", "r")
    data_s = Parse_data(fm3_s)
    Src_coord = Parse_coord(data_s)

    fm3_POI = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 3\POI.txt", "r")
    data_POI = Parse_data(fm3_POI)
    POI_coord = Parse_coord(data_POI)


    Src_dist=distance_vector(Src_coord)
    POI_dist=distance_vector(POI_coord)
  
    for i in Src_dist:
        i.sort()
    for j in POI_dist:
        j.sort()


    fc = open('output3.txt', 'w')
    out=""
    count=0
    for i in range(len(POI_dist)):      #check for distance
        for j in range(len(Src_dist)):
            if len(POI_dist[i])==len(Src_dist[j]):
                ratio=abs(POI_dist[i][0]/Src_dist[j][0])           #RATIO
                flag=0
                for k in range(len(Src_dist[0])):
                    print(ratio , abs(POI_dist[i][k]/Src_dist[j][k]))
                    if abs(POI_dist[i][k]/Src_dist[j][k])!=ratio:
                        flag=1
                        break
                print("\n\n")
                if flag==0:
                    out+=output_format(data_s[j])
                    count+=1
                    
    fc.write(out)

def Milestone4():

    fm3_s= open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 4\Source.txt", "r")
    data_s = Parse_data(fm3_s)
    Src_coord = Parse_coord(data_s)
    
    fm3_POI = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 4\POI.txt", "r")
    data_POI = Parse_data(fm3_POI)
    POI_coord = Parse_coord(data_POI)

    Src_dist=distance_vector(Src_coord)
    POI_dist=distance_vector(POI_coord)
  
    for i in Src_dist:
        i.sort()
    for j in POI_dist:
        j.sort()


    fc = open('output4.txt', 'w')
    out=""
    count=0
    for i in range(len(POI_dist)):  #check for distance
        for j in range(len(Src_dist)):
            if len(POI_dist[i])==len(Src_dist[j]):
                ratio=abs(POI_dist[i][0]/Src_dist[j][0])           #RATIO
                flag=0
                for k in range(len(Src_dist[j])):
                    if abs(POI_dist[i][k]/Src_dist[j][k])!=ratio:
                        flag=1
                        break
                if flag==0:
                    out+=output_format(data_s[j])
                    count+=1
    print(count)
    fc.write(out)


def Milestone5():
    fm3_s= open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 5\Source.txt", "r")
    data_s = Parse_data(fm3_s)
    Src_coord = Parse_coord(data_s)
    
    fm3_POI = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 5\POI.txt", "r")
    data_POI = Parse_data(fm3_POI)
    POI_coord = Parse_coord(data_POI)

    Src_dist=distance_vector(Src_coord)
    POI_dist=distance_vector(POI_coord)
  
    for i in Src_dist:
        i.sort()
    for j in POI_dist:
        j.sort()
    
    fc = open('output5.txt', 'w')
    out=""
    count=0
    for i in range(len(POI_dist)):            #check for distance
        for j in range(len(Src_dist)):
            if len(POI_dist[i])==len(Src_dist[j]):
                ratio=abs(POI_dist[i][0]/Src_dist[j][0])         #RATIO
                flag=0
                for k in range(len(Src_dist[j])):
                    
                    if abs(POI_dist[i][k]/Src_dist[j][k])!=ratio:
                        flag=1
                        break
                if flag==0:
                    out+=output_format(data_s[j])
                    count+=1
    print(count)
    fc.write(out)


def Milestone6():
    fm3_s= open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 6\Source.txt", "r")
    data_s = Parse_data(fm3_s)
    Src_coord = Parse_coord(data_s)
    
    fm3_POI = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 6\POI.txt", "r")
    data_POI = Parse_data(fm3_POI)
    POI_coord = Parse_coord(data_POI)

    Src_dist=distance_vector(Src_coord)
    POI_dist=distance_vector(POI_coord)
  
    for i in Src_dist:
        i.sort()
    for j in POI_dist:
        j.sort()


    fc = open('output6.txt', 'w')
    out=""
    count=0
    for i in range(len(POI_dist)):           #check for distance
        for j in range(len(Src_dist)):
            if len(POI_dist[i])==len(Src_dist[j]):
                ratio=abs(POI_dist[i][0]/Src_dist[j][0])            #RATIO
                flag=0
                for k in range(len(Src_dist[j])):
                    
                    if abs(POI_dist[i][k]/Src_dist[j][k])!=ratio:
                        flag=1
                        break
                if flag==0:
                    out+=output_format(data_s[j])
                    count+=1
    print(count)
    fc.write(out)

def Milestone7():
    fm3_s= open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 7\Source.txt", "r")
    data_s = Parse_data(fm3_s)
    Src_coord = Parse_coord(data_s)
    
    fm3_POI = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 7\POI.txt", "r")
    data_POI = Parse_data(fm3_POI)
    POI_coord = Parse_coord(data_POI)


    Src_dist=distance_vector(Src_coord)
    POI_dist=distance_vector(POI_coord)
  
    for i in Src_dist:
        i.sort()
    for j in POI_dist:
        j.sort()


    fc = open('output7.txt', 'w')
    out=""
    count=0
    for i in range(len(POI_dist)):              #check for distance
        for j in range(len(Src_dist)):
            if len(POI_dist[i])==len(Src_dist[j]):
                ratio=abs(POI_dist[i][0]/Src_dist[j][0])         #RATIO
                flag=0
                for k in range(len(Src_dist[j])):
                    
                    if abs(POI_dist[i][k]/Src_dist[j][k])!=ratio:
                        flag=1
                        break
                if flag==0:
                    out+=output_format(data_s[j])
                    count+=1
    print(count)
    fc.write(out)


    
    






# Milestone1()      #full accuracy and purity
# Milestone2()      #full accuracy and purity
# Milestone3()      #full accuracy and purity
# Milestone4()      #full accuracy and less purity
# Milestone5()      #full accuracy and purity
# Milestone6()      #full accuracy and purity
Milestone7()      #full accuracy and less purity




