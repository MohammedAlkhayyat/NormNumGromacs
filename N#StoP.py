while True:
  filename = input("Enter file name with .gro extention: ")
  try:
    with open(filename, "r") as file:
      print("What is the first residue name (polymer)? ")
      # read the file and do something with it
      break
  except IOError:
    print("Error: Could not open file!, try again!")

pol = input()
sol = input("What is the second residue name (solute)? ")
num = float(input("Enter search radius value (nm): "))

# Open the md.gro file for reading
with open(filename, 'r') as file:
    # Read the file into a list of lines
    lines = file.readlines()
    # Slice the list to exclude the first two and last lines
    lines = lines[2:-1]

# Open the md.gro file for writing
with open(filename, 'w') as file:
    # Write the modified lines back to the file
    file.writelines(lines)

# Open the md.gro file for reading
A =[] 
with open(filename, 'r') as file:
    # Read each line in the file
    for line in file:
        # Split the line into columns
        columns = line.split()
        # Extract column 24 to 53, which contains the x, y, and z coordinates
        coordinates = columns[1:6]
        coordinates_str = ' '.join(coordinates)
        # Split the coordinates into x, y, and z
        if len(coordinates) >= 3:
    # Split the coordinates into x, y, and z
            name, atom , x, y, z = coordinates_str.split()

        else:
    # Handle the case where the sequence does not contain enough values
             print('Error: Not enough coordinates')
        # Print the x, y, and z coordinates
        #print(name, atom , x, y, z)
        A.append([name, atom , x, y, z])

# Create an empty list to store the rows of A that have CE1 in column 1
sol_rows = []

# Loop through the rows of A
for index, row in enumerate(A):
  # If the first column of the current row is CE1, append the last 3 columns to the CE1_rows list
  if row[0] == sol:
    sol_rows.append(row[-3:])

# Create an empty list to store the rows of A that have C1 in column 1
pol_rows = []

# Loop through the rows of A
for index, row in enumerate(A):
  # If the first column of the current row is C1, append the last 3 columns to the C1_rows list
  if row[0] == pol:
    pol_rows.append(row[-3:])

import numpy as np

pol_rows = [[float(col) for col in row] for row in pol_rows]
sol_rows = [[float(col) for col in row] for row in sol_rows]

def num_pol_rows_within_range(pol_rows, row, num):
  num_pol_rows_within_range = 0
  
  for pol_row in pol_rows:
    if all(abs(pol_row - row) <= num for pol_row, row in zip(pol_row, row)):
      num_pol_rows_within_range += 1

  return num_pol_rows_within_range

import math

def num_points_within_radius(pol_rows, sol_rows, radius):
  # Create an empty list to store the results
  num_points_within_radius_list = []

  # Iterate through the elements of the pol_rows list
  for pol_row in pol_rows:
    # Set the counter to 0
    num_points_within_radius = 0

    # Iterate through the elements of the sol_rows list
    for sol_row in sol_rows:
      # Calculate the distance of the current point from the origin
      distance = math.sqrt(math.pow(sol_row[0] - pol_row[0], 2) + math.pow(sol_row[1] - pol_row[1], 2) + math.pow(sol_row[2] - pol_row[2], 2))

      # Check if the distance is within the radius M
      if distance <= radius:
        # Increment the counter if the point is within the radius
        num_points_within_radius += 1

    # Append the number of points within the radius M for the current point in pol_rows to the list
    num_points_within_radius_list.append(num_points_within_radius)

  # Return the list
  return num_points_within_radius_list

listC = num_points_within_radius(pol_rows, sol_rows, num)

results_list = list(zip(pol_rows, listC))

results_list

import csv

my_list = results_list

with open('my_file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in my_list:
        writer.writerow([*row[0], row[1]])
