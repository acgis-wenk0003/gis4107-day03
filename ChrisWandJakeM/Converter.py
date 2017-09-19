#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      chris
#
# Created:     19-09-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#convert miles to kilometres
def miles_to_km(miles):
    km= miles*1.6
    return km

#convert km per hour to metres per second
def kmPerHr_to_mPerSec(kmph):
    m_per_sec= kmph*0.277
    return m_per_sec

def sqmetres_to_hectares(sqmetres):
    """Convert Square Meters to Hectares."""
    hectares = sqmetres/10000
    return hectares

#convert square metres to acres
def sqmetres_acres(sqmetres):
    conv= sqmetres* 0.000247105
    return conv
# calculate bear population
def get_bear_count(BearDensity, area):
    """requires two inputs bear density followed by area in square miles"""
    area_sqkm= area/1000000
    bear_pop=area_sqkm*BearDensity
    return bear_pop

#Decimal Degrees to Degrees Minutes Seconds
def dd_to_dms(dd):
    """requires one input in DD format XX.xxxxx"""
    degrees= int(dd)
    minutes= int((dd-95)*60)
    seconds= (((dd-degrees)*60)-minutes)*60
    return degrees, ":",minutes,seconds



def acres_to_edge_of_square(acres):
    """Convert acres to perimeter of area."""
    perimeter = acres * 254.44
    return perimeter


def dms_to_dd(Degrees,Minutes,Seconds):
    """Output degrees minutes seconds coordinates in decimal degrees format"""
    dd = (Degrees) + (float(Minutes)/60)+(float(Seconds)/3600)
    return dd

def get_fuel_cost(km,mpg,dolperlitre):
    """Convert distance travelled into cost based on
    known distance, mpg and dollars per litre prices."""
    cost = (km)/(mpg*0.425)*(dolperlitre)
    return cost
