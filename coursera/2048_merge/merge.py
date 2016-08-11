"""
Merge function for 2048 game.
""" 
def create_slide_list(line):
    """
    Function that creates a new list with same size but 
    numbers slid over.
    """    
    slide_list = list()
    for num in line:
        if(num != 0):
            slide_list.append(num)
            
    zeros_to_insert = len(line) - len(slide_list)
    slide_list = slide_list + ([0] * zeros_to_insert)
        
    return slide_list
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    merged_list = create_slide_list(line)
    counter = 0
    while counter<len(merged_list)-1:
        if(merged_list[counter] == merged_list[counter+1]):
            merged_list[counter] = merged_list[counter] * 2
            merged_list[counter+1] = 0
            counter += 2
        else:
            counter = counter + 1
           
    return create_slide_list(merged_list)

print merge([2,0,0,2])
