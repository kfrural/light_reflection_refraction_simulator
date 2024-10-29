import math

def calculate_reflection_refraction(angle_of_incidence, n1, n2):
    angle_of_incidence_rad = math.radians(angle_of_incidence)
    reflection_angle = angle_of_incidence  # Reflection angle equals incidence angle

    # Calculate refraction using Snell's Law
    sin_refraction_angle = (n1 / n2) * math.sin(angle_of_incidence_rad)
    
    if abs(sin_refraction_angle) > 1:
        return "Total internal reflection occurs"
    else:
        refraction_angle = math.degrees(math.asin(sin_refraction_angle))
        return f"Reflection Angle: {reflection_angle:.2f}° | Refraction Angle: {refraction_angle:.2f}°"
