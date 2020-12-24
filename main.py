import pandas as pd
import csv
import math
import random


from math import radians, sin, cos, acos
r=pd.read_excel('C:\\Users\\ABHISHEK\\Desktop\\orahi.xlsx','res_location')
l=pd.read_excel('C:\\Users\\ABHISHEK\\Desktop\\orahi.xlsx','Upcoming Orders')

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

def rand():
    return (random.choice([0,1,2]))

def deliveryboy(am,min,cust):
    db=pd.read_excel('C:\\Users\\ABHISHEK\\Desktop\\orahi.xlsx','Delivery Boy Details')
    names=db.to_dict()
    assigned_to=''
    res=[]
    ct=0

    print(names)
    chance=rand()
    totdist=[]
    te=[]
    ct=0

    totdist1=[]
    te1=[]
    ct1=0

    totdist2=[]
    te2=[]
    ct2=0


    if(chance==0):
        assigned_to=names['Name'][0]
        totdist.append(min)
        te.append(am)
        te=sum(te)
        ct+=1
        res.extend([assigned_to,totdist,te,ct])


    elif(chance==1):
        assigned_to=names['Name'][1]
        totdist1.append(min)
        te1.append(am)
        te=sum(te1)

        ct1+=1
        res.extend([assigned_to,totdist1,te1,ct1])



    elif(chance==2):
        assigned_to = names['Name'][2]
        totdist2.append(min)
        te2.append(am)
        te=sum(te2)

        ct2+=1
        res.extend([assigned_to,totdist2,te2,ct2])

    else:
        return

    with open("C:\\Users\\ABHISHEK\\Desktop\\log4.csv","w",newline='\n')as file:
        writer=csv.writer(file,delimiter='-')
        writer.writerow(res)



def coordinate(a1,b1,a2,b2):
    lat1 = math.radians(a1)
    lon1 = math.radians(b1)
    lat2 = math.radians(a2)
    lon2 = math.radians(b2)


    dlon = (lon2 - lon1)
    dlat = (lat2 - lat1)
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    result = 6373.0*c
    return(result)

def distance(lat,lon):
    llat=lat
    llon=lon
    d=[]
    keyy=0

    res_location = r.to_dict()
    rlatitude = res_location['Latitude']
    rlongitude = res_location['Longitute']
    rlat_list=[]
    rlon_list=[]
    for i in range(len(rlatitude)-1):
        rlat_list.append(rlatitude[i])
        rlon_list.append((rlongitude[i]))


    for j in range(len(rlat_list)-1):
        rlat = rlat_list[j]
        rlon = rlon_list[j]
        dist = coordinate(rlat,rlon,llat,llon)
        d.append(dist)
        check=min(d)

    for k in range(len(d)):
        if(check==d[k]):
            keyy=k

    order_location = r['LocationName'][keyy]
    return(min(d))


def order_details(id):
    oId = id - 1
    remember=[]
    remember.append(oId)
    limiter=countX(remember,oId)
    res2=[]
    test = l.to_dict()
    latitude = test['Latitude'][oId]
    longitude = test['Longitute'][oId]
    amount = test['OrderAmount'][oId]
    customer = test['User '][oId]
    res2=[customer,latitude,longitude,'orderrecived']
    if(limiter==2):
        res2 = [customer, latitude, longitude, 'delivery boy assigned']
    elif(limiter==3):
        res2 = [customer, latitude, longitude, 'order picked']
    elif(limiter==4):
        res2 = [customer, latitude, longitude, 'order delivered']
    else:
        res2 = [customer, latitude, longitude, 'orderrecived']

    min_dist = distance(latitude, longitude)
    with open("C:\\Users\\ABHISHEK\\Desktop\\logalpha.csv","w",newline='\n')as file:
        writer=csv.writer(file,delimiter="/")
        writer.writerow(res2)


    deliveryboy(amount,min_dist,customer)


check=(input("Type logs to print delivery details: "))
val=0
condition=''
if(check!="logs" and check!="exit"):
    print("Invalid Input")
    condition=False
elif(check=="exit"):
    print("Have a nice day")
    condition=False
else:
    val =int(input("Enter order id: "))
    if(val>10):
        print("OrderId out of bound")
        condition = False

    else:
        condition=True

while(condition):
    print("Log File Generated")
    order_details(val)

    check = input("Type continue to print additional logs and end to exit out of process: ")

    if(check=="exit" or check!="exit" and check!="continue"):
        if(check=="exit"):
            print("GoodBye")
            condition=False
        else:
            print("Invalid Input")
            condition = False
    else:
        condition=True
        val = int(input("Enter order id: "))





