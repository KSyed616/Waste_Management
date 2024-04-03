from Neighbourhood import Neighbourhood

# create 3 instances of Neighbourhood class called n1, n2, and n3.
# Each have 50, 75, and 50 houses respectively
n1 = Neighbourhood(50)
n2 = Neighbourhood(75)
n3 = Neighbourhood(50)

# adds total number of houses in total from all 3 NH.
# adds the total number of residents.
h_count = n1.total + n2.total + n3.total
res_count = n1.residents() + n2.residents() + n3.residents()

# prints each of the calculated
print(res_count)
print(h_count)