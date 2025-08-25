

# def count_characters(string):
#     char_count = {}
    
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
    
#     return char_count

# # Test the function
# input_string = "minhas rupsi"
# result = count_characters(input_string)

# print("Character count:")
# for char, count in result.items():
#     print(f"{char}: {count}")




# input_string= "minhas rupsi"

# character_count = {char: input_string.count(char) for char in input_string}

# print("Character count:")
# for char, count in character_count.items():
#     print(f"{char}: {count}")




# input_string = "minhas rupsi"

# character_count = {}

# for char in input_string:
#     if char in character_count:
#         character_count[char] += 1
#     else:
#         character_count[char] = 1

# print("Character count:")
# for char, count in character_count.items():
#     print(f"{char}: {count}")




# X=" MINHAS ROSHAN ALI RUPSI"
# count=0
# for index in X:
#     if index==X:
#         count=count+1



X = "MINHAS ROSHAN ALI RUPSI"

count=0

for index in X:
    for Y in X:
        if index==Y:
            count=count+1
    
    print(index,count)
    count=0