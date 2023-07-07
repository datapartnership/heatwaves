

def convert_kelvin_to_fahrenheit(k):
    return 1.8*(k-273.15) + 32


def calculate_heat_index(T, RH):
    HI = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
    return HI

def combine_tmax_rh(tmax, rh):
    tmax=tmax.to_dask_dataframe()
    tmax['Tasmax_F'] = tmax['Tasmax'].apply(lambda x: convert_kelvin_to_fahrenheit(x), meta = ('Tasmax', 'float64'))
    rh = rh.to_dask_dataframe()
    hi = tmax.merge(rh, on = ['time', 'lat', 'lon'])

    return hi


def classify_heat_index(x, t=0, rh=0):
    if x==103 and rh<95 and t>86 and t<90:
        return 3
    elif x>125:
        return 4
    elif x>=104:
        return 3
    elif x>90:
        return 2
    elif x>80:
        return 1
    else:
        return 0