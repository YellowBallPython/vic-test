
# my_res = [17, 20]
# my_res2 = [9, 10]

# reservations = [[10, 13], [15, 17], [20, 21]]
# check_in = 0
# check_out = 1


# def insertion_sort(unsorted_list):
#     for i in range(1, len(unsorted_list)):
#         j = i
#         # both values the same
#         current_res, temp = unsorted_list[i], unsorted_list[i]
#         while unsorted_list[j-1][1] > current_res[0] and j > 0:
#             unsorted_list[j] = unsorted_list[j-1]
#             unsorted_list[j-1] = temp
#             j -= 1
#     return unsorted_list


# sort_res_list = insertion_sort(reservations)


# def make_res(sorted_list, reservation):
#     for i in range(1, len(sort_res_list)):
#         if sorted_list[i-1][check_out] <= reservation[check_in] and reservation[check_out] <= sorted_list[i][check_in]:
#             reservations.append(my_res)
#             return 0
#         else:
#             return 1


# output = make_res(sort_res_list, my_res)
# print(output)


months = {
    1: 'enero',
    2:'febrero',
    3:'marzo',
}

print(months.get(1))