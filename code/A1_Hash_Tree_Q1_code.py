# -*- coding: utf-8 -*-
"""
Created On : Sun Sep 12 2021
Last Modified : Tue Sep 21 2021
Course : MSBD5002 
Assignment : Assignment 01 Question 01 Part (a)

Remarks:
    - this is meant for final submission
"""

### Candidate List is added here
# Add the Candidate List Here
candidate_list=[[1, 2, 3], [1, 4, 5], [1, 2, 4], [1, 2, 5], [1, 5, 9], [1, 3, 6],[2, 3, 4], [2, 5, 9],[3, 4, 5], [3, 5, 6], [3, 5, 9], [3, 8, 9], [3, 2, 6],[4, 5, 7], [4, 1, 8], [4, 7, 8], [4, 6, 7],[6, 1, 3], [6, 3, 4], [6, 8, 9], [6, 2, 1], [6, 4, 3],[6, 7, 9],[8, 2, 4], [8, 9, 1], [8, 3, 6], [8, 3, 7], [8, 4, 7], [8, 5, 1], [8, 3, 1], [8, 6, 2]]



### Define the Hash Function
# Define the Hash Function that will split the item sets
# The hash function will split the item set to either the Left leaf (L), Middle Leaf (M) or the Right Leaf (R)
def hash_function(x):
    if x in [1,4,7]:
        return 'L'
    if x in [2,5,8]:
        return 'M'
    if x in [3,6,9]:
        return 'R'
    else:
        return print('item not in hash')



### This section will prepare the Candidate List before generating the hash tree
# - 1. Sort the Candidate List
# - 2. Remove any duplicates

# Sort the items inside the item set before generating the hash tree
candidate_list_new = []
for item in candidate_list:
    sorted_item = sorted(item)
    candidate_list_new.append(sorted_item)


# Any duplicates after sorting will be removed
candidate_list_new2 = []
for item in candidate_list_new:
    if item not in candidate_list_new2:
        candidate_list_new2.append(item)
        
# The new sorted candidate list is returned to the candidate list variable
candidate_list = candidate_list_new2
# print("(Sorted) Candidate List for Input:")
# print(candidate_list)
print("\n")



### Start Generating the 1st Layer of the Hash Tree
### Summary of Variables Used in the following code:
# - "hash_tree_dict" variable: (Hash Tree Dictionary)
#  - The purpose of "hash_tree_dict" is to compile all the list of candidates according to the layer in the Hash Tree
#  - "hash_tree_dict" variable is not meant for printing but for generating the hash tree to be used internally in the code

# - "hash_tree_list" variable: (Hash Tree List)
#  - "hash_tree_list" sole purpose is to print the hash tree as a nested list at the end of this code

# Initialize the following variables
item = 1 # Start splitting the candidate items according to the 1st item on the list
layerK = 1 # Starting at the 1st layer of the Hash Tree
max_leaf_size = 3 # The maximum leaf size is 3

# Generate the First Layer of the Hash Tree
L_leaf_list = ['K'+str(layerK), 'L']
M_leaf_list = ['K'+str(layerK), 'M']
R_leaf_list = ['K'+str(layerK), 'R']
L_leaf = []
M_leaf = []
R_leaf = []
hash_tree_dict = {'Layer '+str(layerK): []}  # Initialize the 1st layer of the hash_tree dictionary


for item_set in candidate_list: # Iterate over all the item set in the candidate list
    leaf_position = hash_function(item_set[item-1]) # Use the hash function to split the item set 
    if leaf_position == 'L':
        L_leaf.append(item_set) # item set will be appended to the Left Leaf 
    if leaf_position == 'M':
        M_leaf.append(item_set) # item set will be appended to the Middle Leaf
    if leaf_position == 'R':
        R_leaf.append(item_set) # item set will be appended to the Right Leaf
# Finally all the Nodes (Leaves) will be appended to the hash_tree dictionary
L_leaf_list.append(L_leaf)
hash_tree_dict['Layer '+str(layerK)].append(L_leaf_list)
M_leaf_list.append(M_leaf)
hash_tree_dict['Layer '+str(layerK)].append(M_leaf_list)
R_leaf_list.append(R_leaf)
hash_tree_dict['Layer '+str(layerK)].append(R_leaf_list)

# The Nodes (Leaves) are also added to the hash_tree list for printing at the end of the code 
hash_tree_list = [L_leaf,M_leaf,R_leaf]  # Purpose for this variable is for printing the results at the end




### Generate the remaining layers of the Hash Tree
# - The following code will continue to create the remaining layers of the Hash Tree
# - and also iterate over each item in the item set until it is fully iterated (E.g. 3 items in each item set)

# Purpose for this variable is to track and print any linkedlist that stores any leftover items 
linkedlist_counter = 0 
linkedlist_tracker = [] 
# Generate the remaining layers of the Hash Tree
flag = True # While there are still items in the item set not iterated
while flag is True:
    # This section will check the leaf size of each node(Leaf)
    # The output from this section will contain a list of True or False
    # True for Leaf Node size is more than 3
    # False for Leaf Node size is less than or equal to 3        
    leaf_checker = []
    for item_set in hash_tree_dict['Layer '+str(layerK)]: # Check the latest Layer in the hash_tree dictionary
        if len(item_set[2]) > max_leaf_size:
            leaf_checker.append(True)
        else:
            leaf_checker.append(False)
                
    # This section is to decide if need to make a new layer in the Hash Tree
    # Or break from the while loop because iterated over all 3 items in the item set. 
    if any(leaf_checker) is True:
        # If any node (Leaf) size is more than 3
        layerK +=1
        item +=1
        flag = True
        if item > 3: # ensure to check the following item at each layer
            # if all 3 of the items were iterated
            # break from the while loop        
            # print('reset')
            flag = False
            break
            # item = 1
        # print('current item:'+ str(item))
    else:
        # If none of the node (Leaf) size is more than 3
        # break from the while loop        
        flag = False
        # print('End')
        break

    # This section will start to generate the next layer of the hash_tree dictionary 
    leaf_pos = 0 # For Example, start with Left leaf (0), Middle leaf (1) and then Right leaf(2)
    hash_tree_dict['Layer '+str(layerK)]=[]  # Initialize the new Layer in the hash_tree dictionary
    leaf_pos_currentlayer = 0 # This will only be used in the section for adding the nested list into the list for printing
    for leaf in leaf_checker:
        
        # This is section is for keeping track of the index position for the hash_tree list (nested list)
        # To generate the hash_tree list (nested list) for printing        
        if leaf_pos_currentlayer > 2: ##
            leaf_pos_currentlayer = 0 ##

        # This section will generate the following layer of the hash_tree dictionary
        if leaf is True:
                        
            # The Node (Leaf) that has more than 3 item sets will be further split into 3 more Nodes (Leaves)
            # The new layer and the new item sets that were split will be added to the hash_tree dictionary            
            next_candidate_list = hash_tree_dict['Layer '+str(layerK-1)][leaf_pos][2]
            L_leaf_list = ['K'+str(layerK), 'L']
            M_leaf_list = ['K'+str(layerK), 'M']
            R_leaf_list = ['K'+str(layerK), 'R']
            L_leaf = []
            M_leaf = []
            R_leaf = []
            for item_set in next_candidate_list:
                leaf_position = hash_function(item_set[item-1]) # the item set are input into the hash function
                if leaf_position == 'L':
                    L_leaf.append(item_set)
                if leaf_position == 'M':
                    M_leaf.append(item_set)        
                if leaf_position == 'R':
                    R_leaf.append(item_set)
            
            # Finally the new Nodes (Leaves) will be appended to the hash_tree dictionary
            L_leaf_list.append(L_leaf)
            hash_tree_dict['Layer '+str(layerK)].append(L_leaf_list)
            M_leaf_list.append(M_leaf)
            hash_tree_dict['Layer '+str(layerK)].append(M_leaf_list)
            R_leaf_list.append(R_leaf)
            hash_tree_dict['Layer '+str(layerK)].append(R_leaf_list)
            

            
            # This inner section is only for adding the new split nodes into the hash tree list (nested list) for printing
            # If Item 2 in the item set was used to split the items (in the 2nd layer of the hash_tree)
            if item == 2: 
                nested_hash_tree = [L_leaf,M_leaf,R_leaf]
                hash_tree_list[leaf_pos] = nested_hash_tree   
            # If Item 3 in the item set was used to split the items (in the 3rd layer of the hash_tree)
            if item == 3: 
                nested_hash_tree = [L_leaf,M_leaf,R_leaf]
                
                # for Nodes (Leaves) that exceeded the maximum leaf size (3)
                # the extra items are stored into a LinkedList 
                if len(L_leaf) > 3: # For Left Node (Leaf)
                    extraitems = L_leaf[2:len(L_leaf)]
                    linkedlist_counter += 1
                    linkedlist_tracker.append([{'LinkedList '+str(linkedlist_counter):extraitems} ])
                    L_leaf[2:len(L_leaf)] = ['LinkedList '+str(linkedlist_counter)]
                    nested_hash_tree = [L_leaf,M_leaf,R_leaf]
                    
                if len(M_leaf) > 3: # For Middle Node (Leaf)
                    extraitems = M_leaf[2:len(M_leaf)]
                    linkedlist_counter += 1
                    linkedlist_tracker.append([{'LinkedList '+str(linkedlist_counter):extraitems} ])
                    M_leaf[2:len(M_leaf)] = ['LinkedList '+str(linkedlist_counter)]
                    nested_hash_tree = [L_leaf,M_leaf,R_leaf]
                    
                if len(R_leaf) > 3: # For Right Node (Leaf)
                    extraitems = R_leaf[2:len(R_leaf)]
                    linkedlist_counter += 1
                    linkedlist_tracker.append([{'LinkedList '+str(linkedlist_counter):extraitems} ])
                    R_leaf[2:len(R_leaf)] = ['LinkedList '+str(linkedlist_counter)]
                    nested_hash_tree = [L_leaf,M_leaf,R_leaf]

                # This section is to remove any of the empty list that was generated
                # (Due to no new nodes was made at the following new layer)
                # Before the hash tree list (nested list) are printed
                if L_leaf == []:
                    nested_hash_tree.remove([])
                if M_leaf == []:
                    nested_hash_tree.remove([])
                if R_leaf == []:
                    nested_hash_tree.remove([])

                
                # This section will add the finaly results of the nested list to the hash tree list for printing
                # Reminder: hash_tree_list variable is only for printing the final results
                if leaf_pos in [0,1,2]:
                    hash_tree_list[0][leaf_pos_currentlayer] = nested_hash_tree
                if leaf_pos in [3,4,5]:
                    hash_tree_list[1][leaf_pos_currentlayer] = nested_hash_tree
                if leaf_pos in [6,7,8]:
                    hash_tree_list[2][leaf_pos_currentlayer] = nested_hash_tree

        else:
            # The Node (Leaf) that has less than or equal to 3 item sets will be ignored
            # in the New Layer generated in the hash_tree dictionary, 'No Branch' will be added
            # This is to indicate, no new nodes (leaves) was generated.                        
            empty_branch_list = ['K'+str(layerK), 'No Branch',['No Branch']]
            hash_tree_dict['Layer '+str(layerK)].append(empty_branch_list)

        leaf_pos_currentlayer +=1
        leaf_pos +=1


### Final Results of the Hash Tree: 
# Print the hash_tree List to display the generated hash tree    
print('Hash Tree:')
print(hash_tree_list)  
print('\n')  
# Print the LinkedList for Nodes that exceed its maximum size of 3 
print('Linked List:') 
for i in range(0,len(linkedlist_tracker)):
    for m in range(0, len(linkedlist_tracker[i])):
        val = linkedlist_tracker[i][m]['LinkedList '+str(i+1)]
        print_val = []            
        for elem in val:
            print_val.append(str(elem))
        final_val = ' -> '.join(print_val)
        print('LinkedList '+str(i+1)+ ' : '+final_val)


    






