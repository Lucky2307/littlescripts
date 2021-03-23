import math

def dot(a: list, b: list):
    if a[0].__len__() != b.__len__() or a[0].__len__() < 2 or b.__len__() < 2: raise TypeError('Invalid matrix')

    retMatrix = []
    noteMatrix = []
    for x in range(a.__len__()):
        xMatrix = []
        xNoteMatrix = []
        for y in range(b[0].__len__()):
            item = 0
            itemNote = ""
            for i in range(a[x].__len__()):
                item += a[x][i]*b[i][y]
                itemNote += "({} * {}) + ".format(a[x][i], b[i][y])
            xMatrix.append(round(item, 2))
            xNoteMatrix.append(itemNote[:-3])
        noteMatrix.append(xNoteMatrix)
        retMatrix.append(xMatrix)
    return retMatrix, noteMatrix


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

def scale(mat: list, x, y, z = 0):
    scaleMatrix = [
        [x, 0],
        [0, y]
    ]
    if z != 0: 
        scaleMatrix[0].append(0)
        scaleMatrix[1].append(0)
        scaleMatrix.append([0, 0, z])

    return dot(mat, scaleMatrix)

def shear(mat: list, x = 0, y = 0):
    # Two dimensionals only
    retMatrix = ()
    if x != 0:
        shearMatrix = [
            [1, 0],
            [x, 1]
        ]
        retMatrix = dot(mat, shearMatrix)
    if y != 0:
        shearMatrix = [
            [1, y],
            [0, 1]
        ]
        retMatrix = dot(mat, shearMatrix)
    return retMatrix

def transpose(mat: list):
    retMatrix = []
    for x in range(mat[0].__len__()):
        xMatrix = []
        for y in range(mat.__len__()):
            xMatrix.append(mat[y][x])
        retMatrix.append(xMatrix)

    return retMatrix


if __name__ == "__main__":
    # //////////////////////////////
    # // Change matrix value here //
    # //////////////////////////////
    matOne = [
        [2, -2]
    ]
    matTwo = [
        [2, 1],
        [0, 2]
    ]
    matThree = [
        [2, 0],
        [0, 2]
    ]

    mat = dot(matTwo, matThree)
    for m in mat:
        for n in m:
            print(n)
        print("\n")

    scl = scale(matTwo, 2, 2)
    for m in scl:
        for n in m:
            print(n)
        print("\n")

    shr = shear(matTwo, x = 2)
    for m in shr:
        for n in m:
            print(n)
        print("\n")

    trn = transpose(matTwo)
    for m in trn:
        print(m)
    print("\n")