
def get_fuel_cost(km,mpg,dolperlitre):
    """Convert distance travelled into cost based on
    known distance, mpg and dollars per litre prices."""
    cost = (km)/(mpg*0.425)*(dolperlitre)
    return cost

y = get_fuel_cost(100,35,1.3)

print y