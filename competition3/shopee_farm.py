# T = input()
# N, M = [int(x) for x in input().split(" ")]
farms = dict()
# for n in range(N):
#     farms[n] = [0] + [int(x) for x in input().split(" ")]



# def walk_through(side, cur_day):
#     if cur_day == N:
#         return 0
#     cur_farm = farms[cur_day] if side=="left" else farms[cur_day][::-1]
#     cur_health = 0
#     cur_left_health = cur_right_health = 0
#     for cell in range(M+1):
#         cur_health = cur_health + cur_farm[cell]
#         if cell != M:
#             cur_left_health = max(cur_left_health,  cur_health)
#         else:
#             cur_right_health = max(cur_right_health, cur_health)
#     return max(cur_left_health+walk_through("left", cur_day+1), cur_right_health+walk_through("right", cur_day+1))


N, M = 1, 5
farms[0] = [0, -9, -8, 1, 2, 3, 0]

N, M = 2, 3
farms[0] = [0, 1, 4, -5, 0]
farms[1] = [0, -1, -9, 100, 0]


# N,M = 2, 3
# farms[0] = [0, 1, 4, -5, 0]
# farms[1] = [0, -1, -1, 100, 0]

farm = farms[0]
right_health = left_health = cross_health = 0
max_health = 0
for cell in range(M+1):
    right_health = right_health + farm[cell]
    # if cell != M:
    left_health = max(left_health, right_health)
    # else:  
    # cross_health = max(cross_health, cur_health)
    # cross_health = cur_health

for day in range(1, N):
    farm = farms[day]
    left_prefix_sum = right_prefix_sum = from_left_stay_left = from_left_to_right = from_right_stay_right = from_right_to_left = 0
    for cell in range(M+1):
        left_prefix_sum = left_prefix_sum + farm[cell]
        right_prefix_sum = right_prefix_sum + farm[(M-cell)]
        from_left_stay_left = max(from_left_stay_left, left_prefix_sum)
        from_left_to_right = left_prefix_sum
        from_right_stay_right = max(from_right_stay_right, right_prefix_sum)
        from_right_to_left = right_prefix_sum
    right_health = max(right_health+from_right_stay_right, left_health+from_left_to_right)
    left_health = max(left_health+from_left_stay_left, right_health+from_right_to_left)

max_health = max(right_health, left_health)
print(max_health)