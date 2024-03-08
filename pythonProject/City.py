from Neighbourhood import Neighbourhood

n1 = Neighbourhood(50)
n2 = Neighbourhood(75)
n3 = Neighbourhood(50)

h_count = n1.total + n2.total + n3.total
res_count = n1.residents() + n2.residents() + n3.residents()
print(res_count)
print(h_count)

