import numpy as np

from advent.utils import read_data


TEST_DATA = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def get_neighbours(matrix, index):
    dims = matrix.shape
    i, j = index
    n1 = (i - 1, j) if i > 0 else None
    n2 = (i + 1, j) if i < dims[0] - 1 else None
    n3 = (i, j - 1) if j > 0 else None
    n4 = (i, j + 1) if j < dims[1] - 1 else None
    return list(filter(None, [n1, n2, n3, n4]))


def get_basin(lowpoint_idx, heightmap, basin, index=None):
    idx = lowpoint_idx if index is None else index
    neighbours = get_neighbours(heightmap, idx)
    for neighbour in neighbours:
        n = heightmap[neighbour]
        if n == 9 or neighbour in basin:
            continue
        basin.append(neighbour)
        get_basin(lowpoint_idx, heightmap, basin, index=neighbour)
    return basin


def get_basins(lowpoints, heightmap):
    basins = []
    for lowpoint, index in lowpoints:
        basin = get_basin(index, heightmap, [])
        basins.append(basin)
    return basins


def run():
    #data = TEST_DATA
    data = read_data(9)
    heightmap = []
    for line in data:
        heightmap.append(list(map(int, line)))
    heightmap = np.array(heightmap)

    dims = heightmap.shape
    lowpoints = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            n = heightmap[i, j]
            neighbours = get_neighbours(heightmap, (i, j))
            if all(n < heightmap[neighbour] for neighbour in neighbours):
                lowpoints.append((n, (i, j)))

    print(lowpoints)
    print("Sum risk levels: {}".format(sum([lp[0] + 1 for lp in lowpoints])))

    basins = get_basins(lowpoints, heightmap)
    top3 = sorted(basins, key=lambda b: len(b), reverse=True)[:3]
    product = 1
    for basin in top3:
        product *= len(basin)

    print(f"Product of basins sizes: {product}")
