DATA = [[140, 1], [130, 1], [150, 0], [170, 0]]
ANSWER = ['apple', 'apple', 'orange', 'orange', ]
K = 3


def KNN(data, k, new_point):
    distances: list = []
    collate: dict = {}
    for point in data:
        distance = ((point[0] - new_point[0]) ** 2 + (point[1] - new_point[1]) ** 2) ** 0.5
        distances.append([distance, point[1]])
        collate[hash(distance) ^ hash(point[1])] = point
    distances.sort()
    for index, distance_item in enumerate(distances):
        distances[index] = collate[hash(distance_item[0]) ^ hash(distance_item[1])]
    distances = distances[:k]

    # generate possibilities
    possibilities = {}
    for final_distance0 in distances:
        if not possibilities.get(final_distance0[1]):
            possibilities[final_distance0[1]] = 0

    # find majority
    for final_distance1 in distances:
        possibilities[final_distance1[1]] += 1

    # find final
    greatest_connection = [0, 0]
    for each_distance in possibilities:
        if possibilities[each_distance] > greatest_connection[1]:
            greatest_connection = [each_distance, possibilities[each_distance]]

    return greatest_connection[0]


try:
    print(KNN(DATA, K, [140, 1]))
except Exception as e:
    print(f"exception @ {e}")
