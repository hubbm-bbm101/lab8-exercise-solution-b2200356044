import sys
file=open(sys.argv[1],"r")
d={}
for i in file:
    i=i[:-1]
    d[i.split(":")[0]]=list((i.split(":")[1]).split(","))
for j in sys.argv[2].split(","):
    try:
            uni=d[j][0]
            department=d[j][1]
            print("Name:{},University:{},department:{}".format(j,uni,department))
    except:
        print("No record of {} found.".format(j))
