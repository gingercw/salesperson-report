"""Generate sales report showing total melons each salesperson sold."""


salespeople = []    # Creates an empty list that will later store names 
melons_sold = []    # Creates an empty list that will later store the number of melons sold
                    # Suggestion: Create a dictionary instead since the salespeople and melon_sold data should be connected

f = open('sales-report.txt')        # Opens sales report document. Suggestion: Rename "f" to be more descriptive. 
for line in f:                      # Loops through each line in the document. Suggestion: Create a function.
    line = line.rstrip()            # Suggestion: Combine lines for stripping and splitting. 
    entries = line.split('|')       

    salesperson = entries[0]        # Assigns first item in line as salesperson
    melons = int(entries[2])        # Assigns third item in line as melon count and makes it an integer

    if salesperson in salespeople:                  
        position = salespeople.index(salesperson)   # Finds the index number of the salesperson in the salespeople list

        melons_sold[position] += melons             # Adds up melons sold per salesperson
    else:
        salespeople.append(salesperson)             # Adds salespeople and melons sold to respective lists
        melons_sold.append(melons)


for i in range(len(salespeople)):                                   # Uses index number in loop
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')         # Formats data as a sentence
