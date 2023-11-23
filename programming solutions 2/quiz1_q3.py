from collections import defaultdict
# --------------------------------------
# Function to convert Edge List to Adjacency List
def edge_list_to_adjacency_list(edge_list):
    adj_list=defaultdict(list)
    
    for e1,e2 in edge_list:
        print(e1,e2)
        adj_list[e1].append(e2)
        
    return adj_list

"""    for i in range(len(adj_matrix)):
        tmp=[]
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j]!=0:
                tmp.append(j)
        adj_list[i]=tmp"""

	# Write your code here to convert the edge list to an adjacency list.

    

# Test case
edge_list_sample = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

# --- Student Section to Write Code ---
# Write your code for the conversion here
result_adj_list = edge_list_to_adjacency_list(edge_list_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")
# --------------------------------------
