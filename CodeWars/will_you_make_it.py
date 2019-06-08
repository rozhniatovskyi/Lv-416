def zero_fuel(distance_to_pump, mpg, fuel_left):
    capacity = mpg * fuel_left
    if (capacity - distance_to_pump) >= 0:
        return True
    return False
