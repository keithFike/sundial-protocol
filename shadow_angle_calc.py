#! /usr/bin/python3

from math import sin, tan, atan, degrees, radians

def calculateShadowAngle(time: float, latitude: float) -> float:
    DEGREES_PER_HOUR: int = 15
    NOON: int = 12
    
    #time from noon if noon is 0
    meridian_adjusted_time: float = time - NOON
    
    #angle of shadow assuming 0 latitude
    absolute_hour_angle: float = meridian_adjusted_time * DEGREES_PER_HOUR
    
    #angle of shadow accounting for latitude
    relative_hour_angle: float = degrees(atan(tan(radians(absolute_hour_angle)) * sin(radians(latitude))))

    return relative_hour_angle


if __name__ == "__main__":
    print(calculateShadowAngle(13, 40.376896))
