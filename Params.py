import math

class Params:
    PIXELS = 1920
    d = 0.06 # in cm

    ALPHA = math.radians(26.91)
    tan_ALPHA = math.tan(ALPHA)

    BETA1 = math.radians()
    BETA2 = math.radians()
    BETA3 = math.radians()
    BETA4 = math.radians()

    tan_BETA1 = math.tan(BETA1)
    tan_BETA2 = math.tan(BETA2)
    tan_BETA3 = math.tan(BETA3)
    tan_BETA4 = math.tan(BETA4)

    a_correction = 1
    b_correction = 1

    camera_diff = 0.04 # in cm

def sigma_tan(duo):
    match duo:
        case 1:
            return (Params.tan_BETA1 + Params.tan_BETA2)
        case 2:
            return (Params.tan_BETA2 + Params.tan_BETA3)
        case 3:
            return (Params.tan_BETA3 + Params.tan_BETA4)
    return 0