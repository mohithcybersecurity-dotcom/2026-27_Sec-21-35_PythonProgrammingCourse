class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter speed (km/h): "))
    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Speed must be between 0 and 120.")
    print("Speed accepted:", speed)
except InvalidSpeedError as err:
    print("Custom error:", err)