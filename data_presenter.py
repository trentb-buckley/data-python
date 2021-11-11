






open_file = open("CupcakeInvoices.csv")

# for i in open_file:
    # print(i)

# for i in open_file:
#     i = i.strip()
#     flavor = i.split(',')
#     print(flavor[2])





# for i in open_file:
#     i = i.strip()
#     q = i.split(',')
#     # print(q[4])

# numArr = []
# for i in open_file:
#     i = i.strip()
#     q = i.split(',')
#     numArr.append(int(q[4]))
#     for j in numArr:
#         int = numArr[j]
#         sum += float(int)
# print(sum)


# open_file.close()

# open_file = open("CupcakeInvoices.csv")

# total_c = 0
# total_s = 0
# total_v = 0
# for line in open_file:
#     line = line.strip()
#     values = line.split(',')
#     for value in values:
#         if



# # import pandas as pd
# total=0
# choc_total = 0
# van_total=0
# for line in cupcake:
#     split_line = line.strip().split(',')



# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# fig, ax = plt.subplots()
# flavors = ['strawberry', 'chocolate', 'vanilla']
# totals = [straw_total, choc_total, van_total]
# ax.bar(flavors, totals)

# # x_ticks = np.append(ax.get_xticks(), 0)
# # ax.set_xticks(x_ticks)

# plt.show()

import pandas as pd
cupcake = []
for data in open_file:
    data = data.strip()
    values = data.split(",")
    first_name, last_name, type, quantity, price = values
    myTuple = (first_name,last_name,type,quantity,price)
    cupcake.append(myTuple)
# print(cupcake)
index = []
for i in range(len(cupcake)):
    index.append(str(i + 1))
# print(index)

cupcake_df = pd.DataFrame(cupcake, columns = ['first_name', 'last_name', 'type', 'quantity', 'price'], index = index)
# print(cupcake_df.shape)
for index in range(cupcake_df.shape[1]):
    columnSeriesObj = cupcake_df.iloc[:, index]
    print('Column Contents: ', columnSeriesObj.values)
