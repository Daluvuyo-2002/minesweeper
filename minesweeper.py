#minesweeper.py

def minesweeper(list):
    for row in range(len(list)): # Convert '-' to 0
        for col in range(len(list[row])):
            if list[row][col] == " - ":
                list[row][col] = 0

    for row in range(len(list)):# Convert to minesweeper format
        for col in range(len(list[row])):

            if list[row][col] != " # ":
                
                # West Position ----------------------------------------------------------------------
                list_2 = list[row] # Create a list to be observed
                prev_value = list_2[0] # Store the previous value to be reset after list is checked
                list_2[0] = "*" # Changing the first variable to a marker

                index = list_2.index(list_2[col])

                if index > 0:
                    if list_2[col - 1] == " # ":
                        list_2[col] += 1
                
                # Update list
                list_2[0] = prev_value
                list[row] = list_2

                # East Position ---------------------------------------------------------------------
                list_2 = list[row] # Create a list to be observed
                prev_value = list_2[-1] # Store the previous value to be reset after list is checked
                list_2[-1] = "*" # Create an end marker for the list
                
                if list_2[col] != list_2[-1]:
                    if list_2[col + 1] == " # ":
                        list_2[col] += 1
                
                # Update list
                list_2[-1] = prev_value
                list[row] = list_2
                
                # North Postion ----------------------------------------------------------------------
                if list.index(list[row]) != 0:
                    list_2 = list[row - 1] # Create a list to be observed
                    list_3 = list[row] # Create a list to be changed

                    if list_2[col] == " # " and list_3[col] != " # ":
                        list_3[col] += 1
                    
                    # Update list
                    list[row] = list_3
                
                # South Position ----------------------------------------------------------------------
                if list.index(list[row]) < (len(list) - 1):
                    list_2 = list[row + 1] # Create a list to be observed
                    list_3 = list[row] # Create a list to be changed

                    if list_2[col] == " # " and list_3[col] != " # ":
                        list_3[col] += 1
                    
                    # Update list
                    list[row] = list_3

                # North West Position -----------------------------------------------------------------
                if list.index(list[row]) != 0:
                    list_2 = list[row - 1] # Create a list to be observed
                    list_3 = list[row] # Create a list to be changed

                    prev_value = list_3[0] # Store the previous value to be reset after list is checked
                    list_3[0] = "*" # Changing the first variable to a marker

                    index = list_3.index(list_3[col])

                    if index > 0 and list_2[col - 1] == " # " and list_3[col] != " # ":
                        list_3[col] += 1
                    
                    # Update list
                    list_3[0] = prev_value
                    list[row] = list_3
                
                # North East Position -----------------------------------------------------------------
                if list.index(list[row]) != 0:
                    list_2 = list[row - 1] # Create a list to be observed
                    list_3 = list[row] # Create a list to be changed

                    prev_value = list_3[-1] # Store the previous value to be reset after list is checked
                    list_3[-1] = "*" # Changing the first variable to a marker

                    if list_3[col] != "*" and list_2[col + 1] == " # " and list_3[col] != " # ":
                        list_3[col] += 1
                    
                    # Update list
                    list_3[-1] = prev_value
                    list[row] = list_3
                
                # South East Position -----------------------------------------------------------------
                if list.index(list[row]) < (len(list) - 1):
                    list_2 = list[row + 1] # Create a list to be observed
                    list_3 = list[row] # Create a list to be changed

                    prev_value = list_3[-1] # Store the previous value to be reset after list is checked
                    list_3[-1] = "*" # Changing the first variable to a marker

                    if list_3[col] != "*" and list_2[col + 1] == " # " and list_3[col] != " # ":
                        list_3[col] += 1
                    
                    # Update list
                    list_3[-1] = prev_value
                    list[row] = list_3
                
                # North West Position -----------------------------------------------------------------
                if list.index(list[row]) < (len(list) - 1):
                    list_2 = list[row + 1] # Create a list to be observed
                    list_3 = list[row] # Create a list to be changed

                    prev_value = list_3[0] # Store the previous value to be reset after list is checked
                    list_3[0] = "*" # Changing the first variable to a marker

                    index = list_3.index(list_3[col])

                    if index > 0 and list_2[col - 1] == " # " and list_3[col] != " # ":
                        list_3[col] += 1
                    
                    # Update list
                    list_3[0] = prev_value
                    list[row] = list_3

        print(list[row])        
    
test_list = [[ " - " , " - " , " - " , " # " , " # " ] , [ " - " , " # " , " - " , " - " , " - " ] , [ " - " , " - " , " # " , " - " , " - " ] , [ " - " , " # " , " # " , " - " , " - " ] , [ " - " , " - " , " - " , " - " , " - " ]]

minesweeper(test_list)