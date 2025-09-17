import numpy as np

def wgs84_to_lambert (lon: np.array , lat : np.array) -> tuple :
    """ Convert WGS 84 coordinates to an Austrian Lambert Conic Conformal
    Projection ( lcc)
    EPSG code : 31287 , see https :// epsg .io /31287

    Parameters :
        lon (np. array ): Vector containing wgs 84 longitudes
        lat (np. array ): Vector containing wgs 84 latitudes

    Returns :
        x, y (np. array ): Vectors containing lcc coordinates
    """

    # Constants
    E0 = 400000 # in meters
    N0 = 400000 # in meters
    FSP = 49 # fsp = First Standard Parallel ('PHI1') 49°N
    SSP = 46 # ssp = second standard parallel ('PHI2') 46°N
    LoO = 47.5 # loo = latitude of origin ('PHI0') 47.5°N
    CM = 13.3333 # cm = central meridian ('lambda0') 13°20'E (13.3333333333°E)
    
    # Convertions
    phi1 = np.radians(FSP)
    phi2 = np.radians(SSP)
    phi0 = np.radians(LoO)
    phi = np.radians(lat)
    lm0 = np.radians(CM) # lambda0
    lm = np.radians(lon) # lambda
    R = 6377397.155 # Semi-major axis (Bessel 1841)
    
    # Step 1: Compute the Cone Constant 'n'
    n = np.log(np.cos(phi1) / np.cos(phi2)) / np.log(np.tan(np.add(np.pi/4, phi2/2)) / np.tan(np.add(np.pi/4, phi1/2)))
    #print(f'n = {n}')
    
    # Step 2: Compute the Scale Factor 'F'
    F = np.multiply(np.cos(phi1), np.power(np.tan(np.add(np.pi/4, phi1/2)), n)) / n
    #print(f'F = {F}')
    
    # Step 3: Compute the Reference Radius 'p0'
    p0 = np.multiply(R, F) / np.power(np.tan(np.add(np.pi/4, phi0/2)), n)
    #print(f'p0 = {p0}')
    
    # Step 4: Compute the Radius for the given Latitude
    p = np.multiply(R, F) / np.power(np.tan(np.add(np.pi/4, phi/2)), n)
    #print(f'p = {p}')
    
    # Step 5: Compute the Angular Difference from the Central Meridian (theta)
    theta = np.multiply(n, np.subtract(lm, lm0))
    #print(f'theta ={theta}') 
    
    # Step 6: Compute the Final Projected Coordinates: E, N; E0, N0 = false Easting and false Northing
    x = np.add(E0, np.multiply(p, np.sin(theta))) # Easting
    y = np.add(N0, np.subtract(p0, np.multiply(p, np.cos(theta))))  # Northing
    #print(f'Easting (E) = {x}')
    #print(f'Northing (N) = {y}')
    
    
    return x, y