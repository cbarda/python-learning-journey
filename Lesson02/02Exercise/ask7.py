#δοκιμστε τις παρακατω πραξεις
#int + float
an_int = 5
a_float = 3.14
print(an_int + a_float)  # This will output 8.14
#int + string
a_string = "Hello"
#print(a_string + an_int)  # Uncommenting this line will cause an error
print(a_string + str(an_int))  # This will output "Hello5"
#float + string
print(a_string + str(a_float))  # This will output "Hello3.14"
#string + string
print(a_string + " World!")  # This will output "Hello World!"
#int + int
print(an_int + 10)  # This will output 15
#float + float
print(a_float + 2.86)  # This will output 6.0
#int + bool
a_bool = True #In general 0 = False and 1 = True
print(an_int + a_bool)  # This will output 6
#float + bool
print(a_float + a_bool)  # This will output 4.14
#string + bool
print(a_string + str(a_bool))  # This will output "HelloTrue"
#bool + bool
print(a_bool + True)  # This will output 2
