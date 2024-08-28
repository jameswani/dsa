
# _________________Recursive Problem Solving___________________
# 1. Check for termination cases/base cases
# 2. Do the processing: For back tracking, mark the current state as visited for pruning and optimization
# 3. Move to recursive cases: Call the recursive function on all variants
# 4. Reset side effects: Undo changes to avoid unexpected bugs especially with backtracking

# __________________Backtracking Foundations_____________________
# 1. Visualize each state of the solution as a node in a tree
# 2. Pruning: Eliminate possibilities that won't lead to a solution
# 3. Partial Candidate: Differentiate between partially and fully completed solutions for clearer thinking

# Template for solving backtracing problems
# 1. Define the problem: Understand requirements and constraints. This adds clarity and 
#    helps your problem solving flow more smoothly
# 2. Define the state space tree: Visualize the problem as a tree with nodes representing 
#    solution states
# 3. Recursively explore solutions: Use recursion to explore possibilities
#    
# 4. Prune unsuccessful paths: Abandon paths that don't meet constraints early
# 
# 5. Combine solutions: Merge partial solutions into the final solution

def find_sum(n): 
    if n == 1:
        return 1
    return n + find_sum(n-1)

print(find_sum(5))