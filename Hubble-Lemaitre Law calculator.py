hubble_constant = 70

def calculate_galaxy_speed(distance):
    speed = hubble_constant * distance
    return speed


distance_to_galaxy = 50
estimated_speed = calculate_galaxy_speed(distance_to_galaxy)

print(f"A galaxy {distance_to_galaxy} Mpcaway is moving away from us at") ;