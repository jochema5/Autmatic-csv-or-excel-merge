#Import the necessary libraries
import pandas as pd
import glob

#we create the glob list of files to read, the asterisk (*) 
# replaces any combination of characters. A question mark (?) 
# replaces a character. If nothing is excluded, it reads all files in format

#For read csv
csv_example = glob.glob("example*.csv")

#For read xlsx
xlsx_example = glob.glob("example*xlsx")

#See the table
xlsx_example

csv_example

#Create the list where save the results
list_example =[]

 #Read the files using the bucle
for i in csv_example:
    ss = pd.read_csv(i)
    list_example.append(ss)

#CSee the list read
list_ss

#Concatenate the files
df =pd.concat(list_example, ignore_index=True)

#Enviamos el archivo a un csv
df.to_csv("example.csv")
