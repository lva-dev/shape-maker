from math import sin, cos, radians as rad
import numpy as np


def obj_to_array(path, x=True, y=True, z=True):
    object_file = open(path, 'r')
    coordinates = np.array([])
    for line in object_file.readlines():
        if line.startswith('v '):
            vertex = np.array(line[3:].split())
            coordinates = np.append(arr=coordinates, values=vertex, axis=0)
    coordinates = coordinates.reshape((-1, 3)).astype('f').tolist()
    if not x:
        coordinates = np.delete(coordinates, 0, 1)
    if not y:
        coordinates = np.delete(coordinates, 1, 1)
    if not z:
        coordinates = np.delete(coordinates, 2, 1)
    return coordinates.tolist()


if __name__ == '__main__':
    path_to_object_file: str = r"C:\Users\adote\Documents\untitled.obj"

    # Converting OBJ to numpy array.
    print(f'vertices = arr((')
    for vertex in obj_to_array(path_to_object_file, z=False):
        print(f'{vertex}', end='')
        print(',')
    print('))')

    print("-------------------------------------------")

    # Manually creating shapes.
    circle = np.array(
            [(cos(rad(theta)), sin(rad(theta))) for theta in range(0, 360, 1)]
            , dtype='f')
    circle += 1
    circle /= 2
    circle = circle.tolist()
    print(f'vertices = arr((')
    for vertex in circle:
        print(f'{vertex}', end='')
        print(',')
    print('))')
