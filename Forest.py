a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = int(input())

# Tính số bước tối thiểu để đi theo hướng Bắc - Đông - Nam - Tây
min_steps_north = min(a, c, k)
k -= min_steps_north
min_steps_east = min(b, d, k)
k -= min_steps_east
min_steps_south = min(a, c, k)
k -= min_steps_south
min_steps_west = min(b, d, k)

# Tổng số bước tối thiểu cần đi
min_steps = min_steps_north + min_steps_east + min_steps_south + min_steps_west

print(min_steps)
