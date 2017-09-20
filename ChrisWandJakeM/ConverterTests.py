
import Converter
reload(Converter)

#test miles to kilometres

def test_miles_to_km():
    test_m_to_k= Converter.miles_to_km(10)
    print "10 miles", "=", test_m_to_k, "Km"
#test convert km per hour to metres per second
def test_kmPerHr_to_mPerSec():
    testkmperh_to_mpersec= Converter.kmPerHr_to_mPerSec(100)
    print "100 Km/hr", "=", testkmperh_to_mpersec, "m/s"
#Convert Square Metres to Hectares
def test_sqmetres_to_hectares():
    test_sqm_to_hectares = Converter.sqmetres_to_hectares(10000)
    print "10000 Sq. m.", "=", test_sqm_to_hectares, "Hectares"
#test convert square metres to acres
def test_sqmetres_to_acres():
    test_sqm_to_acres= Converter.sqmetres_acres(10000)
    print "10000 square metres =", test_sqm_to_acres, "acres."
#Calculate edge length from acres
def test_acres_to_edge_of_square():
    test_acres2perimeter = Converter.acres_to_edge_of_square(2)
    print "Edge length of 2 acres square is", test_acres2perimeter, "metres."
#test calculate bear population
def test_get_bear_count():
    test_bears= Converter.get_bear_count(4,10000000)
    print "When bear density is 4 bears per square kilometre and the area is 10000000 square metres then the probable number of bears is:", test_bears

#Convert degrees minutes seconds coordinates to decimal degrees format.
def test_dms_to_dd():
    test_dd = Converter.dms_to_dd(95,25,05)
    print "95:25:05 =", test_dd,"decimal degrees."

#test convert Decimal Degrees to Degrees Minutes Seconds
def test_dd_to_dms():
    test_degrees, test_minutes, test_seconds= Converter.dd_to_dms(95.41805)
    print test_degrees, ":", test_minutes, ":", test_seconds

#Calculate fuel cost with known distance, mpg and dollars per litre price.
def test_get_fuel_cost():
    test_fuel_cost = Converter.get_fuel_cost(100,35,1.3)
    print "100 km at 35 mi/gal and $1.3 per L will cost $", test_fuel_cost


#call functions
test_miles_to_km()
test_kmPerHr_to_mPerSec()
test_sqmetres_to_hectares()
test_sqmetres_to_acres()
test_acres_to_edge_of_square()
test_get_bear_count()
test_dms_to_dd()
test_dd_to_dms()
test_get_fuel_cost()


