from iteration_utilities import unique_justseen

s = 'ttttuuuurrrrttttlllleeee'
turtle = s[0] + s[4] + s[8] + s[12] + s[16] + s[23]
print(turtle)

s = 'ttttuuuurrrrttttlllleeee'
turtle = s[-24] + s[-20] + s[-16] + s[-12] + s[-8] + s[-4]  
print(turtle)

turtle = unique_justseen(s)
print(turtle)


# slim = s[5] + s[8] + s[6] + s[1]

# print(slim)































# string = 'hallo world'
# string_list = string.split() 
# print(string_list)

# small_art = string[0:5]
# print(small_art)