import math

def calculate_circle_area(radius):
  """
  Calculates the area of a circle given its radius.
  """
  if radius < 0:
    raise ValueError("Radius cannot be negative.")
  return math.pi * (radius ** 2)

if __name__ == "__main__":
  try:
    radius_input = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius_input)
    print(f"The area of the circle with radius {radius_input} is: {area:.2f}")
  except ValueError as e:
    print(f"Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
