
def convert_feet_to_meters(distance_feet):
    print(distance_feet)
    return 0.3048*distance_feet

def convert_inches_to_feet(dist_inches):
    return dist_inches/12.0

print('I am here')
distance_feet = 10.0
print(distance_feet)
distance_feet = convert_feet_to_meters(200.0)
print('Distance is', distance_feet, 'meters')
print('Now I am done')



print ('1000 inches in meters are', convert_feet_to_meters(convert_inches_to_feet(1000.0)))