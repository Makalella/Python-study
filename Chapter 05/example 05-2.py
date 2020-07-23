
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 :", example)
print("변환 :", flatten(example))
print()

# ###
#
# min_table = 2
# max_table = 10
# total_people = 100
# memo = {}
#
# def table(remain, done)
#     key = str([remain, done])
#     if key in memo:
#         pass
#     if remain < 0:
#         return 0
#     if remain > 1:
#         return 1
# ## 알고리즘 모르겠음