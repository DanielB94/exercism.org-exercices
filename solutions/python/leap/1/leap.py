def leap_year(year):
    """ if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
       return False, All this logics resumed in one line using booleans"""

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
