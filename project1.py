import math
# WELCOMING THE USER
print("WELCOME.THIS IS A GEODETIC CALCULATOR.IT IS DESIGNED BY ESSQ/2017,IN LEADERSHIP  OF DAVE & JOSH .\n")
print ("CHOOSE WHAT YOU WANT TO FIND.PRESS 1 FOR GEODETIC COORDINATES,2 FOR RECTANGULAR COORDINATES,3 FOR ADJUSTMENT COMPUTATIONS OR 4 FOR PHOTOGRAMMETRY COMPUTATIONS")
work_choice = int(input("ENTER YOUR CHOICE FOR WHAT YOU NEED TO FIND:"))

if work_choice==1:
    # PROMPTING THE USER TO ENTER THE RECTANGULAR COORDINATES
    x = float(input("PLEASE ENTER YOUR RECTANGULAR LATITUDE VALUE:"))
    y = float(input("PLEASE ENTER YOUR RECTANGULAR LONGITUDE VALUE:"))
    z = float(input("PLEASE ENTER YOUR RECTANGULAR HEIGHT VALUE:"))

    # PROMPTING THE USER TO CHOOSE A REFERENCE ELLIPSOID
    print ("CHOOSE THE REFERENCE ELLIPSOID IN USE[1,2].1 IF CLARKE 1858,AND 2 IF CLARKE 1880.")
    reference_ellipsoid = int(input("Enter your choice of reference ellipsoid:"))
    if reference_ellipsoid==1:
        a = 6378294
        b = 6356618
    elif reference_ellipsoid==2:
        a = 6378249.145
        b = 6356514.967
    else:
        print("TRY AGAIN")

    # READING AND PROCESSING THE GEODETIC VALUES.
    # THE PROCESS USES THE INDIRECT METHOD TO FIND LATITUDE.
    # PROCESSING THE GEODETIC LONGITUDE
    long = math.degrees(math.atan(y / x))

    # PROCESSING THE GEODETIC LATITUDE
    e = (a**2 - b**2)/a**2
    c = 1 + ((e ) / (1 - e))
    lat1 = math.degrees(math.atan(z / math.sqrt(x**2 + y**2)) * c)
    v = a / (math.sqrt(1 - (e*(math.sin(math.radians(lat1)))**2)))
    lat2 = math.degrees(math.atan((z + (v*e*(math.sin(math.radians(lat1))))) / math.sqrt(x**2 + y**2)))
    v1 = a / math.sqrt(1 - (e*(math.sin(math.radians(lat2)))**2))
    lat3 = math.degrees(math.atan((z + (v1*e*(math.sin(math.radians(lat2))))) / math.sqrt(x**2 + y**2)))
    v2 =  a / math.sqrt(1 - (e*(math.sin(math.radians(lat3)))**2))
    lat4 =  math.degrees(math.atan((z + (v2*e*(math.sin(math.radians(lat3))))) / math.sqrt(x**2 + y**2)))
    v3 = a / math.sqrt(1 - (e*(math.sin(math.radians(lat4))**2)))
    lat5 = math.degrees(math.atan((z + (v3*e*(math.sin(math.radians(lat4))))) / math.sqrt(x**2 + y**2)))
    v4 = a / math.sqrt(1 - (e*(math.sin(math.radians(lat5))**2)))
    lat6 = math.degrees(math.atan((z + (v4*e*(math.sin(math.radians(lat5))))) / math.sqrt(x**2 + y**2)))
    v5 =  a / math.sqrt(1 - (e*(math.sin(math.radians(lat6))**2)))
    lat7 =  math.degrees(math.atan((z + (v5*e*(math.sin(math.radians(lat6))))) / math.sqrt(x**2 + y**2)))
    # DETERMINING THE FINAL GEODETIC LATITUDE VALUE
    if lat1 == lat2:
        lat = lat2
    elif lat3 == lat2:
        lat = lat3
    elif lat3 == lat4:
        lat = lat4
    elif lat4 == lat5:
        lat = lat5
    elif lat5 == lat6:
        lat = lat6
    elif lat6 == lat7:
        lat = lat7
    else:
        lat = lat7


    # PROCESSING THE GEODETIC HEIGHT
    v =  a / (math.sqrt(1 - (e*(math.sin(math.radians(lat)))**2)))
    h = (math.sqrt(x**2 + y**2) / math.cos(math.radians(lat))) - v
    # WRITING OUTPUT

    print ("GEODETIC LATITUDE:\n",lat)
    print ("GEODETIC LONGITUDE:\n",long)
    print ("GEODETIC HEIGHT:\n",h)

    # THIS PART PROCESSES RECTANGULAR COORDINATES FROM GEODETIC COORDINATES
elif work_choice==2:
    alpha = float(input("ENTER THE GEODETIC LATITUDE VALUE:"))
    lambda1 = float(input("ENTER THE GEODETIC LONGITUDE VALUE:"))
    height = float(input("ENTER THE GEODETIC HEIGHT VALUE:"))
    print("CHOOSE THE REFERENCE ELLIPSOID IN USE,PRESS 1 IF CLARK1858,2 IF CLARKE 1880")
    REFERENCE_ELLIPSOID = int(input("ENTER THE REFERENCE ELLIPSOID IN USE:"))
    if REFERENCE_ELLIPSOID==1:
        a = 6378294
        b = 6356618
    elif REFERENCE_ELLIPSOID==2:
        a = 6378249.145
        b = 6356514.967

    else:
        print("TRY AGAIN")
    e = (a**2 - b**2) / a**2
    v = a / (math.sqrt(1 - (e * (math.sin(math.radians(alpha))) ** 2)))
    X = (v + height)* math.cos(math.radians(alpha)) * math.cos(math.radians(lambda1))
    Y = (v + height)* math.cos(math.radians(alpha)) * math.sin(math.radians(lambda1))
    Z = (v * (1 - e) + height) * math.sin(math.radians(alpha))

    # WRITING OUTPUT
    print ("RECTANGULAR LATITUDE,X:\n",X)
    print ("RECTANGULAR LONGITUDE,Y:\n",Y)
    print ("RECTANGULAR HEIGHT,Z:\n",Z)

elif work_choice==3:
    print ("WHAT DO YOU NEED TO FIND IN ADJUSTMENT COMPUTATIONS?PRESS 1 FOR MPV,2 FOR MEAN ERROR,3 FOR STD.DEVIATION OF MEASUREMENTS.")
    COMPUTATION_CHOICE = int(input("ENTER WHAT YOU NEED TO FIND:"))
    if COMPUTATION_CHOICE==1:
        print ("THIS COMPUTATIONAL CALCULATOR WORKS WITH 20 OBSERVATIONAL VALUES ONLY. KINDLY NOTE THAT,IF YOUR VALUES ARE LESS THAN 20,INPUT THE REMAINING VALUES AS ZEROS.")
        N = int(input("PLEASE ENTER THE NUMBER OF OBSERVATIONS MADE:"))
        measurement1 = float(input("ENTER MEASUREMENT 1:"))
        measurement2 = float(input("ENTER MEASUREMENT 2:"))
        measurement3 = float(input("ENTER MEASUREMENT 3:"))
        measurement4 = float(input("ENTER MEASUREMENT 4:"))
        measurement5 = float(input("ENTER MEASUREMENT 5:"))
        measurement6 = float(input("ENTER MEASUREMENT 6:"))
        measurement7 = float(input("ENTER MEASUREMENT 7:"))
        measurement8 = float(input("ENTER MEASUREMENT 8:"))
        measurement9 = float(input("ENTER MEASUREMENT 9:"))
        measurement10 = float(input("ENTER MEASUREMENT 10:"))
        measurement11 = float(input("ENTER MEASUREMENT 11:"))
        measurement12 = float(input("ENTER MEASUREMENT 12:"))
        measurement13 = float(input("ENTER MEASUREMENT 13:"))
        measurement14 = float(input("ENTER MEASUREMENT 14:"))
        measurement15 = float(input("ENTER MEASUREMENT 15:"))
        measurement16 = float(input("ENTER MEASUREMENT 16:"))
        measurement17 = float(input("ENTER MEASUREMENT 17:"))
        measurement18 = float(input("ENTER MEASUREMENT 18:"))
        measurement19 = float(input("ENTER MEASUREMENT 19:"))
        measurement20 = float(input("ENTER MEASUREMENT 20:"))
        # FINDING MPV
        MPV = (measurement1+measurement2+measurement3+measurement4+measurement5+measurement6+measurement7+measurement8+measurement9+measurement10+measurement11+measurement12+measurement13+measurement14+measurement15+measurement16+measurement17+measurement18+measurement19+measurement20)/N
        print ("MPV IS:",MPV)
    elif COMPUTATION_CHOICE==2:
        print("THIS COMPUTATIONAL CALCULATOR WORKS WITH 20 OBSERVATIONAL VALUES ONLY..INCASE YOUR OBSERVATIONS ARE LESS THAN 20,USE 0 AS THE VALUES OF OTHER MISSING MEASUREMENTS TO TOTAL 20 MEASUREMENTS.")
        N = int(input("ENTER THE NUMBER OF OBSERVATIONS:"))
        measurement1 = float(input("ENTER MEASUREMENT 1:"))
        measurement2 = float(input("ENTER MEASUREMENT 2:"))
        measurement3 = float(input("ENTER MEASUREMENT 3:"))
        measurement4 = float(input("ENTER MEASUREMENT 4:"))
        measurement5 = float(input("ENTER MEASUREMENT 5:"))
        measurement6 = float(input("ENTER MEASUREMENT 6:"))
        measurement7 = float(input("ENTER MEASUREMENT 7:"))
        measurement8 = float(input("ENTER MEASUREMENT 8:"))
        measurement9 = float(input("ENTER MEASUREMENT 9:"))
        measurement10 = float(input("ENTER MEASUREMENT 10:"))
        measurement11 = float(input("ENTER MEASUREMENT 11:"))
        measurement12 = float(input("ENTER MEASUREMENT 12:"))
        measurement13 = float(input("ENTER MEASUREMENT 13:"))
        measurement14 = float(input("ENTER MEASUREMENT 14:"))
        measurement15 = float(input("ENTER MEASUREMENT 15:"))
        measurement16 = float(input("ENTER MEASUREMENT 16:"))
        measurement17 = float(input("ENTER MEASUREMENT 17:"))
        measurement18 = float(input("ENTER MEASUREMENT 18:"))
        measurement19 = float(input("ENTER MEASUREMENT 19:"))
        measurement20 = float(input("ENTER MEASUREMENT 20:"))
        # FINDING THE MPV
        MPV = (measurement1+measurement2+measurement3+measurement4+measurement5+measurement6+measurement7+measurement8+measurement9+measurement10+measurement11+measurement12+measurement13+measurement14+measurement15+measurement16+measurement17+measurement18+measurement19+measurement20)/N
        # FINDING THE ERROR,E
        E1 = measurement1 / MPV
        E2 = measurement2 / MPV
        E3 = measurement3 / MPV
        E4 = measurement4 / MPV
        E5 = measurement5 / MPV
        E6 = measurement6 / MPV
        E7 = measurement7 / MPV
        E8 = measurement8 / MPV
        E9 = measurement9 / MPV
        E10 = measurement10 / MPV
        E11 = measurement11 / MPV
        E12 = measurement12 / MPV
        E13 = measurement13 / MPV
        E14 = measurement14 / MPV
        E15 = measurement15 / MPV
        E16 = measurement16 / MPV
        E17 = measurement17 / MPV
        E18 = measurement18 / MPV
        E19 = measurement19 / MPV
        E20 = measurement20 / MPV

        Em = (E1+E2+E3+E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16+E17+E18+E19+E20) / N
        print ("MEAN ERROR IS:",Em)
    elif COMPUTATION_CHOICE==3:
        print("THIS COMPUTATIONAL CALCULATOR WORKS WITH 20 OBSERVATIONAL VALUES ONLY. INCASE YOUR VALUES ARE LESS THAN 20,PLEASE GO BACK AND PRESS 1 TO FIND THE MPV,NOTE THE MPV AND USE IT AS THE SUBSTITUTE FOR MISSING VALUES TO MAKE THE OBSERVATIONAL VALUES TO 20")
        N = 20
        measurement1 = float(input("ENTER MEASUREMENT 1:"))
        measurement2 = float(input("ENTER MEASUREMENT 2:"))
        measurement3 = float(input("ENTER MEASUREMENT 3:"))
        measurement4 = float(input("ENTER MEASUREMENT 4:"))
        measurement5 = float(input("ENTER MEASUREMENT 5:"))
        measurement6 = float(input("ENTER MEASUREMENT 6:"))
        measurement7 = float(input("ENTER MEASUREMENT 7:"))
        measurement8 = float(input("ENTER MEASUREMENT 8:"))
        measurement9 = float(input("ENTER MEASUREMENT 9:"))
        measurement10 = float(input("ENTER MEASUREMENT 10:"))
        measurement11 = float(input("ENTER MEASUREMENT 11:"))
        measurement12 = float(input("ENTER MEASUREMENT 12:"))
        measurement13 = float(input("ENTER MEASUREMENT 13:"))
        measurement14 = float(input("ENTER MEASUREMENT 14:"))
        measurement15 = float(input("ENTER MEASUREMENT 15:"))
        measurement16 = float(input("ENTER MEASUREMENT 16:"))
        measurement17 = float(input("ENTER MEASUREMENT 17:"))
        measurement18 = float(input("ENTER MEASUREMENT 18:"))
        measurement19 = float(input("ENTER MEASUREMENT 19:"))
        measurement20 = float(input("ENTER MEASUREMENT 20:"))
        # FINDING THE MPV
        MPV = (measurement1 + measurement2 + measurement3 + measurement4 + measurement5 + measurement6 + measurement7 + measurement8 + measurement9 + measurement10 + measurement11 + measurement12 + measurement13 + measurement14 + measurement15 + measurement16 + measurement17 + measurement18 + measurement19 + measurement20) / N
        # FINDING THE ERROR,E
        E1 = measurement1 / MPV
        E2 = measurement2 / MPV
        E3 = measurement3 / MPV
        E4 = measurement4 / MPV
        E5 = measurement5 / MPV
        E6 = measurement6 / MPV
        E7 = measurement7 / MPV
        E8 = measurement8 / MPV
        E9 = measurement9 / MPV
        E10 = measurement10 / MPV
        E11 = measurement11 / MPV
        E12 = measurement12 / MPV
        E13 = measurement13 / MPV
        E14 = measurement14 / MPV
        E15 = measurement15 / MPV
        E16 = measurement16 / MPV
        E17 = measurement17 / MPV
        E18 = measurement18 / MPV
        E19 = measurement19 / MPV
        E20 = measurement20 / MPV
        #FINDING STD DEVIATIONS
        P1 = (E1 * E1)/ (N - 1)
        P2 = (E2 * E2) / (N - 1)
        P3 = (E3 * E3) / (N - 1)
        P4 = (E4 * E4) / (N - 1)
        P5 = (E5 * E5) / (N - 1)
        P6 = (E6 * E6) / (N - 1)
        P7 = (E7 * E7) / (N - 1)
        P8 = (E8 * E8) / (N - 1)
        P9 = (E9 * E9) / (N - 1)
        P10 = (E10 * E10) / (N - 1)
        P11 = (E11 * E11) / (N - 1)
        P12 = (E12 * E12) / (N - 1)
        P13 = (E13 * E13) / (N - 1)
        P14 = (E14 * E14) / (N - 1)
        P15 = (E15 * E15) / (N - 1)
        P16 = (E16 * E16) / (N - 1)
        P17 = (E17 * E17) / (N - 1)
        P18 = (E18 * E18) / (N - 1)
        P19 = (E19 * E19) / (N - 1)
        P20 = (E20 * E20) / (N - 1)
        # FINDING FINAL STD.DEVIATION
        P = P1+P2+P3+P4+P5+P6+P7+P8+P9+P10+P11+P12+P13+P14+P15+P16+P17+P18+P19+P20

        print ("STANDARD DEVIATION IS:",P)
    else:
        print ("INVALID CHOICE.TRY AGAIN")
else:
    print ("WE ARE STILL DEVELOPING. COME BACK LATER FOR PHOTOGRAMMETRY COMPUTATIONS. ")


















