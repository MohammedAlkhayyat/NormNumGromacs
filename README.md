The N#StoP.py is the code that gives you the csv that contains the number of solutes around each monomer chain. 

Download the code and run the command 

```
python3 N#StoP.py'
```

Enter then the gro file name and the polymer and solute names

The first part of the code prompts the user to input the name of the file, and then attempts to open the file and read it in. If the file cannot be opened, an error message is displayed and the user is prompted to try again.

Once the file has been successfully opened, the code asks the user to input the names of two different residues, referred to as the "polymer" and the "solute". It then asks the user to input a search radius value in nanometers.

The code then opens the file again and reads it into a list of lines, excluding the first two and last lines. It then opens the file again in write mode and writes the modified list of lines back to the file.

Next, the code opens the file again in read mode and reads each line in the file. It splits each line into columns, extracts columns 24 to 53, which contain the x, y, and z coordinates, and splits the coordinates into x, y, and z. If the coordinates do not contain at least 3 values, an error message is displayed.

The code then creates two empty lists, one to store rows of the file that contain the first residue name (polymer), and another to store rows of the file that contain the second residue name (solute). It then loops through the rows of the file and appends the last 3 columns (the x, y, and z coordinates) to the appropriate list if the first column matches the name of the residue.

Next, the code imports the NumPy library and converts the rows in the pol_rows and sol_rows lists from strings to floats. It then defines a function named num_pol_rows_within_range which takes 3 arguments: pol_rows, row, and num. This function loops through the pol_rows list and counts the number of rows whose x, y, and z coordinates are within a certain distance (specified by the num argument) of the x, y, and z coordinates of the row argument.

The code then defines another function named num_points_within_radius which takes 3 arguments: pol_rows, sol_rows, and radius. This function loops through the elements of the pol_rows list, and for each element it loops through the elements of the sol_rows list. For each pair of elements, it calculates the distance between the x, y, and z coordinates and compares it to the radius. If the distance is less than or equal to the radius, it increments a counter. After all pairs have been compared, the function appends the final value of the counter to a list and returns the list.

Finally, the code calls the num_points_within_radius function, passing it the pol_rows, sol_rows, and num variables as arguments, and prints the result.
