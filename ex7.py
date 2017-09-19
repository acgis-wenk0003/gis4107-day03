
def dms_to_dd(Degrees,Minutes,Seconds):
    """Output degrees minutes seconds coordinates in decimal degrees format"""
    dd = (Degrees) + (float(Minutes)/60)+(float(Seconds)/3600)
    return dd

y = dms_to_dd(95,25,05)

print y