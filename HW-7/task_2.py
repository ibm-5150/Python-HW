def new_sort(*args, r = False):	
	sorted_args = sorted(args, reverse = r)
	print(sorted_args)
args = input().split()
new_sort(*args, r = False) 
#if r = False - sorted list; r = True - reverse sorted list;
