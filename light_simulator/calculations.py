import math

def calculate_reflection(angle):
    # According to the law of reflection
    return angle

def calculate_refraction(angle_of_incidence, n1, n2):
    try:
        angle_of_incidence_rad = math.radians(angle_of_incidence)
        sin_angle_of_refraction = (n2 / n1) * math.sin(angle_of_incidence_rad)
        
        if abs(sin_angle_of_refraction) > 1:
            return "Total internal reflection occurred."
        
        angle_of_refraction_rad = math.asin(sin_angle_of_refraction)
        angle_of_refraction = math.degrees(angle_of_refraction_rad)
        
        return angle_of_refraction
    except ValueError:
        return "Total internal reflection occurred."
def calculate_reflection_refraction(angle, n1, n2):
    angle_of_reflection = calculate_reflection(angle)
    angle_of_refraction = calculate_refraction(angle, n1, n2)

    return (
        f"Angle of Reflection: {angle_of_reflection:.2f} degrees\n"
        f"Angle of Refraction: {angle_of_refraction:.2f} degrees" if isinstance(angle_of_refraction, float) else angle_of_refraction
    )
