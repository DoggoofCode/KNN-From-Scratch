DATA = [[140, 1], [130, 1], [150, 0], [170, 0]]
ANSWER = ['apple', 'apple', 'orange', 'orange', ]
K = 3


def KNN(data, k, new_point, answer):
    distances: list = []
    collate: dict = {}
    for index, point in enumerate(data):
        distance = ((point[0] - new_point[0]) ** 2 + (point[1] - new_point[1]) ** 2) ** 0.5
        distances.append(distance)
        collate[distance] = answer[index]
    distances.sort()
    for index, dist in enumerate(distances):
        distances[index] = collate[dist]
    distances = distances[:k]

    # generate possibilities
    possibilities = {}
    for label in distances:
        if not possibilities.get(label):
            possibilities[label] = 0

    # find majority
    for label in distances:
        possibilities[label] += 1

    # find final
    greatest_connection = ['', 0]
    for each_distance in possibilities:
        if possibilities[each_distance] > greatest_connection[1]:
            greatest_connection = [each_distance, possibilities[each_distance]]

    return greatest_connection[0]

    # distances.sort()
    # for index, distance_item in enumerate(distances):
    #     distances[index] = collate[hash(distance_item[0]) ^ hash(distance_item[1])]
    # distances = distances[:k]



try:
    print(KNN(DATA, K, ["INSERT VALUE", "INSERT VALUE"], ANSWER))
except Exception as e:
    print(f"exception @ {e}")
