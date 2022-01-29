# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}

def l_system(initial, rules, generation): 
	current = initial # current value is set to initial

	for _ in range(0, generation): # a for loop for iterating from 0 to the number that is the current generation
		result = "" # result is set to an empty string

		for state in current: # a for loop that iterates for each letter in the current string 
			result += rules.get(state, state) # gets the new string for the current state string (A or B) from the rules dictionary and adds it to previous strings in result

		current = result # current is assigned the value of the new string result

	return current # returns the generation of the string required and stops the function

for i in range(0, 10): # for loop to iterate 10 times 
	print( "{}: {}".format(i, l_system(initial, rules, i)) ) # outputs a the current generation string to the screen

