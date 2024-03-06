#select the mult tables u want to calc ;

multiplication_table = int(input("Enter the multiplication table you want like 2, 3, 4.: "))

caluclating_using_lambda = lambda y : y*multiplication_table

range_numbers = range(1,13)

map_result = list(map(caluclating_using_lambda,range_numbers))
 
print(f"your answers are the following {map_result}")
