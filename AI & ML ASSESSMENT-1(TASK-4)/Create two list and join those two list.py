
# Consider three lists
social=['history','civics','economics','geography']
languages=['hindi','english']
others=['subject1']

# Let's join elements within a List
# Example 1: Using join(), Join strings in a list with '-' delimiter.
print('-'.join(social) )

# Example 2: Using join() with map(), with '-' delimiter.
print('-'.join(map(str,social)))

# Let's join two lists
# Example 1: Using append()
for i in languages:
    social.append(i) 
print("Joined Lists: ",social)

# Example 2: Using extend()
social.extend(languages) 
print("Joined Lists: ",social)

# Let's join two or more lists

# Example 1: Using itertools.chain()
import itertools
print("Joined Lists: ",list(itertools.chain (social,languages,others)))

# Example 2: Using * operator
print("Joined Lists: ",[*social, *languages])

# Example 3: Using + operator
print("Joined Lists: ",social+languages+others)
