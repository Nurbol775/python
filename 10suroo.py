def calculate_diameters(radii):
    diameters = [2 * radius for radius in radii]
    return diameters

input_radii = [1, 2, 3]  
output_diameters = calculate_diameters(input_radii)  
print(output_diameters)  
