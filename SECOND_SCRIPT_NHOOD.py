#!/usr/bin/env python3

from shapely.geometry import Point
from check_nhood import check_nhood as cnd
from geopy.geocoders import Nominatim
import sys
import pandas as pd

df = pd.read_csv('./Reentry-Master-120119.csv', encoding = "ISO-8859-1")



print(df.info())
#print(df.info())

def get_lat_long(address):
#    print(address)
    try:
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        location = geolocator.geocode(address)
        points = [Point(location.longitude, location.latitude)]
#        print(points[0])
        for point in points:
            return address, cnd(point), str(location.latitude), str(location.longitude)
    except: 
        return address,('nan', 'nan'), str(location.latitude), str(location.longitude)
    
f = open('Reentry-Master-Test-120119.csv','w')
f.write('ID, Organization, Department_Program, Address, Suite, City, State, Zip, County, Phone, Neighborhood,'+
        'Quadrant, Latitude, Longitude, Website, Type_Facility, Type, Type2, Notes\n')
for k in range(len(df)):
    if str(df['Latitude'][k]) != 'nan':
        f.write(str(df['ID'][k])+','+str(df['Organization'][k])+','+str(df['Department_Program'][k])+','+
                str(df['Address'][k])+','+str(df['Suite'][k])+','+str(df['City'][k])+','+ 
                str(df['State'][k])+','+str(int(df['Zip'][k]))+','+
                str(df['County'][k])+','+str(df['Phone'][k])+','+
                str(df['Neighborhood'][k])+','+str(df['Quadrant'][k])+','+str(df['Latitude'][k])+','+str(df['Longitude'][k])+','+
                str(df['Website'][k])+','+str(df['Type_Facility'][k])+','+str(df['Type'][k])+','+str(df['Type2'][k])+','+
                str(df['Notes'][k])+'\n')
        print(str(df['ID'][k])+','+str(df['Organization'][k])+','+str(df['Department_Program'][k])+','+
                str(df['Address'][k])+','+str(df['Suite'][k])+','+str(df['City'][k])+','+ 
                str(df['State'][k])+','+str(int(df['Zip'][k]))+','+
                str(df['County'][k])+','+str(df['Phone'][k])+','+
                str(df['Neighborhood'][k])+','+str(df['Quadrant'][k])+','+str(df['Latitude'][k])+','+str(df['Longitude'][k])+','+
                str(df['Website'][k])+','+str(df['Type_Facility'][k])+','+str(df['Type'][k])+','+str(df['Type2'][k])+','+
                str(df['Notes'][k]))
        print('')
    else:       
        try:
            addr = str(str(df['Address'][k])+' '+ str(df['City'][k])+' '+str(df['State'][k])+' '+ str(int(df['Zip'][k])))
            aa = get_lat_long(addr)
#            print(aa)
            f.write(str(df['ID'][k])+','+str(df['Organization'][k])+','+str(df['Department_Program'][k])+','+
                str(df['Address'][k])+','+str(df['Suite'][k])+','+str(df['City'][k])+','+ 
                str(df['State'][k])+','+str(int(df['Zip'][k]))+','+
                str(df['County'][k])+','+str(df['Phone'][k])+','+
                str(aa[1][0])+','+str(aa[1][1])+','+str(aa[2])+','+str(aa[3])+','+
                str(df['Website'][k])+','+str(df['Type_Facility'][k])+','+str(df['Type'][k])+','+str(df['Type2'][k])+','+
                str(df['Notes'][k])+'\n')
            print(str(df['ID'][k])+','+str(df['Organization'][k])+','+str(df['Department_Program'][k])+','+
                str(df['Address'][k])+','+str(df['Suite'][k])+','+str(df['City'][k])+','+ 
                str(df['State'][k])+','+str(int(df['Zip'][k]))+','+
                str(df['County'][k])+','+str(df['Phone'][k])+','+
                str(aa[1][0])+','+str(aa[1][1])+','+str(aa[2])+','+str(aa[3])+','+
                str(df['Website'][k])+','+str(df['Type_Facility'][k])+','+str(df['Type'][k])+','+str(df['Type2'][k])+','+
                str(df['Notes'][k]))
            print('')
        except:
            f.write(str(df['ID'][k])+','+str(df['Organization'][k])+','+str(df['Department_Program'][k])+','+
                str(df['Address'][k])+','+str(df['Suite'][k])+','+str(df['City'][k])+','+ 
                str(df['State'][k])+','+str(df['Zip'][k])+','+
                str(df['County'][k])+','+str(df['Phone'][k])+','+
                str(df['Neighborhood'][k])+','+str(df['Quadrant'][k])+','+str(df['Latitude'][k])+','+str(df['Longitude'][k])+','+
                str(df['Website'][k])+','+str(df['Type_Facility'][k])+','+str(df['Type'][k])+','+str(df['Type2'][k])+','+
                str(df['Notes'][k])+'\n')
            print(str(df['ID'][k])+','+str(df['Organization'][k])+','+str(df['Department_Program'][k])+','+
                str(df['Address'][k])+','+str(df['Suite'][k])+','+str(df['City'][k])+','+ 
                str(df['State'][k])+','+str(df['Zip'][k])+','+
                str(df['County'][k])+','+str(df['Phone'][k])+','+
                str(df['Neighborhood'][k])+','+str(df['Quadrant'][k])+','+str(df['Latitude'][k])+','+str(df['Longitude'][k])+','+
                str(df['Website'][k])+','+str(df['Type_Facility'][k])+','+str(df['Type'][k])+','+str(df['Type2'][k])+','+
                str(df['Notes'][k]))
            print('')
            
            
f.close()             