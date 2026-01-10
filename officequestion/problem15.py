# Write a function which take string as a paramter and return the dictionary which contain the counting of each character in string
# Example:
# string : "Aarti"
# Output: {"a":2,"r":1,"t":1,"i":1}




name = str(input("Enter your name: "))


# def char_count(name):
#     name = name.lower()
    
#     count = {}

#     for char in name:
#         if char in count:
#             count[char] += 
        
#          count[char] = name.count(char)
    
#     return char_count
    
# #char_count("Aarti")   
#     #my_name = {}
# #print("The counting of each character is: ")
# print(char_count("Aarti")) 

#correct code
def char_count(name):
    name = name.lower()
    
    count = {}
    
    for char in name:
        if char in count:
            count[char] += 1
            
        else:
            count[char] = 1 
        
        #count[char] = name.count(char)    
    
    #return char_count
    return count
print(char_count(name))