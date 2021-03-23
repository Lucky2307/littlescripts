import math

def dot(a: list, b: list):
    if a[0].__len__() != b.__len__() or a[0].__len__() < 2 or b.__len__() < 2: raise TypeError('Invalid matrix')

    retMatrix = []
    for x in range(a.__len__()):
        xMatrix = []
        for y in range(b[0].__len__()):
            item = 0
            for i in range(a[x].__len__()):
                item += a[x][i]*b[i][y]
            xMatrix.append(round(item, 2))
        retMatrix.append(xMatrix)
    return retMatrix


def rotation(mat: list, angle: int):
    angleRadian = math.radians(angle)
    rotMatrix = [
        [math.cos(angleRadian), -math.sin(angleRadian)],
        [math.sin(angleRadian), math.cos(angleRadian)]
    ]
    return dot(mat, rotMatrix)

def translate(mat: list, x, y, z = 0):
    for xMat in mat:
        xMat[0] += x
        xMat[1] += y
        if xMat.__len__() == 3: xMat[2] += z
    return mat


if __name__ == "__main__":
    # //////////////////////////////
    # // Change matrix value here //
    # //////////////////////////////
    matOne = [
        [2, 3],
        [1, 4],
        [2, 1]
    ]
    matTwo = [
        [3, 1, 2],
        [2, 4, 2]
    ]


    mat = dot(matOne, matTwo)
    for i in mat: print(i)

    rotated = rotation(matOne, 90)
    for i in rotated: print(i)

    translated = translate(matOne, 2, 3)
    for i in translated: print(i)