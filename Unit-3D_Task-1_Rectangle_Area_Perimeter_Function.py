def area_perimeter(length,breadth):
    area=length*breadth
    perimeter=2*(length+breadth)
    return area,perimeter
area,perimeter=area_perimeter(3,5)
print(f"Area:{area}")
print(f"Perimeter:{perimeter}")