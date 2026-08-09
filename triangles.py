with open("triangles.in") as read:
	n = int(read.readline())

	points = []

	for _ in range(n):
		x, y = map(int, read.readline().split())
		points.append((x, y))

answer = 0
areas = []

for i in range(n):

	crux_x, crux_y = points[i]

	x_endpoints = []
	y_endpoints = []

	for j in range(n):
		x_endpoint, y_endpoint = points[j]
		if x_endpoint == crux_x:
			y_endpoints.append(y_endpoint)
	for j in range(n):
		x_endpoint, y_endpoint = points[j]
		if y_endpoint == crux_y:
			x_endpoints.append(x_endpoint)

	x_endpoints.sort()
	y_endpoints.sort()

	small_x = x_endpoints[0] 
	big_x = x_endpoints[len(x_endpoints)-1]
	small_y = y_endpoints[0]
	big_y = y_endpoints[len(y_endpoints)-1]

	if crux_x >= 0:
		if small_x >= 0:
			small_dist_x = abs(small_x - crux_x)
		else:
			small_dist_x = abs(crux_x) + abs(small_x)
		if big_x >= 0:
			big_dist_x = abs(big_x - crux_x)
		else:
			big_dist_x = abs(crux_x) + abs(big_x)
	else:
		if small_x >= 0:
			small_dist_x = abs(small_x) + abs(crux_x)
		else:
			small_dist_x = abs(crux_x - small_x)
		if big_x >= 0:
			big_dist_x = abs(big_x) + abs(crux_x)
		else:
			big_dist_x = abs(crux_x - big_x)

	if crux_y >= 0:
		if small_y >= 0:
			small_dist_y = abs(small_y - crux_y)
		else:
			small_dist_y = abs(crux_y) + abs(small_y)
		if big_y >= 0:
			big_dist_y = abs(big_y - crux_y)
		else:
			big_dist_y = abs(crux_y) + abs(big_y)
	else:
		if small_y >= 0:
			small_dist_y = abs(small_y) + abs(crux_y)
		else:
			small_dist_y = abs(crux_y - small_y)
		if big_y >= 0:
			big_dist_y = abs(big_y) + abs(crux_y)
		else:
			big_dist_y = abs(crux_y - big_y)


	distance_x = max(big_dist_x, small_dist_x)
	distance_y = max(small_dist_y, big_dist_y)

	area = float(distance_x) * float(distance_y)
	area /= 2
	areas.append(area)

areas.sort()
area = areas[len(areas)-1]
answer = 2 * area
answer = int(answer)

with open("triangles.out", "w") as write:
	print(answer, file = write)
