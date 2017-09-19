arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

max_glass=-9999
for i in range(4):
	for j in range(4):
		sum_temp=(arr[i][j]+arr[i][j+1]+arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
		max_glass=max(max_glass,sum_temp)

print max_glass
