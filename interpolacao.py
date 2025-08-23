import numpy as np

def get_points(path: str):
    points_array = np.genfromtxt(path, delimiter=',', dtype=[('x', float), ('y', float)])
    return points_array

def first_degree_interpolation(p0: tuple, p1: tuple):
    m = (p1['y'] - p0['y']) / (p1['x'] - p0['x'])
    b = ((p1['x'] * p0['y']) - (p0['x'] * p1['y'])) / (p1['x'] - p0['x'])

    line = np.array((m, b), dtype=[('m', float), ('b', float)])
    return line

def linear_function(params: tuple, x: float):
    y: float = (params['m'] * x) + params['b']
    return y

def simpson_integration(intervals: int, function_params: tuple, integration_limits: tuple):
    step = (integration_limits[1] - integration_limits[0]) / intervals
    accumulator: float = 0

    for i in range(intervals):
        f_i = linear_function(function_params, (i * step) + integration_limits[0])

        if i == 0:
            accumulator += f_i
            continue
        
        if i == intervals:
            accumulator += f_i
            continue
        
        if i % 2 == 0:
            accumulator += 2 * f_i
        else:
            accumulator += 4 * f_i
    
    integral_approximation: float = accumulator * (step / 3)
    return integral_approximation

POINTS_PATH = 'points.csv'
SUBINTERVALS = 1000
GOOGLE_MAPS_AREA = 642000

points = get_points(POINTS_PATH)

# f(x) = m*x + b
lines = np.array([], dtype=[('m', float), ('b', float)])
areas = []

for i in range(len(points) - 1):
    line = first_degree_interpolation(points[i], points[i+1])
    lines = np.append(lines, line)

    area = simpson_integration(SUBINTERVALS, line, [points[i]['x'], points[i+1]['x']])
    areas.append(area)

total_area = abs(sum(areas))
relative_error = 100 * abs((total_area - GOOGLE_MAPS_AREA) / GOOGLE_MAPS_AREA)

print(f'\nÁrea total através da integração das retas interpoladas com {SUBINTERVALS} subintervalos:')
print(f'{round(total_area, 3)} m²\n')
print('Área real dada pelo Google Maps:')
print(f'{GOOGLE_MAPS_AREA} m²\n')
print('Erro relativo entre o calculado e a área do Google Maps:')
print(f'{round(relative_error, 2)} %')
