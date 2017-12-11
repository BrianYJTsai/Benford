#  File: Benford.py

#  Description: Program verifies tests Benfords Law. Input is a text file of with data sets and the program outputs the frequency
#  of the first digit of each number.

#  Student Name: Brian Tsai

#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 4/29/17

#  Date Last Modified: 4/29/17

def main():
	# create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore the first line
  header = in_file.readline()

  # Iterate over each line
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    
    # get the last element that is the population number
    pop_num = pop_data[-1]
    
    # first_digit is the first digit of the number
    first_digit = pop_num[0]
    
    # Increase the frequency of the number which corresponds to the key
    pop_freq[first_digit] +=1

  # Count the total number of numbers 
  total_count = 0
  for number in pop_freq:
  	total_count += pop_freq[number]

  # Format the table
  print(format("Digit", "<10s"), end = " ")
  print(format("Count", "<10s"), end = " ")
  print("%")

  # Iterate over each item in the dictionary
  for number in pop_freq:
  	# Output the key and value
  	print(format(number, "<10s"), end = " ")
  	print(format(pop_freq[number], "<10d"), end = " ")
  	
  	# percent_freq holds the frequency of each digit
  	percent_freq = pop_freq[number] / total_count
  	percent_freq = percent_freq  * 100
  	
  	# Output the new frequency
  	print(format(percent_freq, "0.1f"))
  	
  # close the file
  in_file.close()
main()	