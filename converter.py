

def sqmetres_to_hectares(sqmetres):
    """Convert Square Meters to Hectares."""
    hectares = sqmetres/10000
    return hectares

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