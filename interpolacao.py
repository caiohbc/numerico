import numpy as np

# Interpolação linear, gerando 12 retas
# Integrar as retas usando método de simpson nos intervalos correspondentes
# Considerar corretamente retas cuja área está fora do polígono
# Calcular a diferença entre o valor interpolado e o valor real

def get_points(path: str):
    points_array = np.genfromtxt(path, delimiter=',', dtype=[('x', np.float64), ('y', np.float64)])
    return points_array

def first_degree_interpolation(p0: tuple, p1: tuple):
    m = (p1['y'] - p0['y'])/(p1['x'] - p0['x'])
    b = ((p1['x'] * p0['y']) - (p0['x'] * p1['y']))/(p1['x'] - p0['x'])

    line = np.array((m, b), dtype=[('m', np.float64), ('b', np.float64)])
    
    return line

POINTS_PATH = 'points.csv'
points = get_points(POINTS_PATH)

lines = np.array([], dtype=[('m', np.float64), ('b', np.float64)])

for i in range(len(points) - 1):
    line = first_degree_interpolation(points[i], points[i+1])
    lines = np.append(lines, line)

print(lines)