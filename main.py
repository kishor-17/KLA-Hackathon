from datetime import datetime
import collections

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

def output_format(inp):
    data=""
    for i in inp:
        data+=i
    return data

def Parse_coord_str(fm2_s):
    st=[]
    for i in fm2_s:
        points1=i[3][7:]
        #print(points1)
        #coord=points1.split("  ")
        st.append(points1)
    return st


def Parse_coord(data):
    POI_coord = []
    for i in data:
        points1=i[3][7:]
        #print(points1)
        coord=points1.split("  ")
        #print(coord)
        co=[]
        for i in coord:
            s=i.split(" ")
            cod = []
            cod.append(int(s[0]))
            cod.append(int(s[1]))
            co.append(cod)
        #print(co)
        POI_coord.append(co)
    return POI_coord


def Milestone2():
    fm2_s= open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 2\Source.txt", "r")
    data_s = Parse_data(fm2_s)
    POI_coord = Parse_coord(data_s)
    
    #print(POI_coord[0],POI_coord[1])

    fm2_POI = open("G:\\PSG TECH\PLACEMENT RESOURCES\Student_Input_2023_PSG_CIT\Milestone_Input\Milestone_Input\Milestone 2\POI.txt", "r")
    data_POI = Parse_data(fm2_POI)
    Src_coord = Parse_coord(data_POI)

    #print(Src_coord)

    Src_str=Parse_coord_str(data_s)
    POI_str=Parse_coord_str(data_POI)
    #print(POI_str)

    out=""

    for i in range(len(POI_str)):
        for j in range(len(Src_str)):
            if collections.Counter(POI_str[i]) == collections.Counter(Src_str[j]):
                #print(Src_str[j])
                out+=output_format(data_s[j])
    # print(out)
                
    fc = open('output2.txt', 'w')
    fc.write(out)
    
    







Milestone2()




