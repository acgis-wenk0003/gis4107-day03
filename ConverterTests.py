
import converter
reload(converter)

#Convert Square Metres to Hectares
def test_sqmetres_to_hectares():
    test_sqm_to_hectares = converter.sqmetres_to_hectares(10000)
    print "10000 Sq. m.", "=", test_sqm_to_hectares, "Hectares"

#Calculate edge length from acres
def test_acres_to_edge_of_square():
    test_acres2perimeter = converter.acres_to_edge_of_square(2)
    print "Edge length of 2 acres square is", test_acres2perimeter, "metres."

#Convert degrees minutes seconds coordinates to decimal degrees format.
def test_dms_to_dd():
    test_dd = converter.dms_to_dd(95,25,05)
    print "95:25:05 =", test_dd,"decimal degrees."

#Calculate fuel cost with known distance, mpg and dollars per litre price.
def test_get_fuel_cost():
    test_fuel_cost = converter.get_fuel_cost(100,35,1.3)
    print "100 km at 35 mi/gal and $1.3 per L will cost $", test_fuel_cost


#call functions
test_sqmetres_to_hectares()
test_acres_to_edge_of_square()
test_dms_to_dd()
test_get_fuel_cost()


