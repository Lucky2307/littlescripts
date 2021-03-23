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
                itemNote += "({} * {}) + ".format(round(a[x][i]), round(b[i][y]))
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
    if mat[0].__len__() == 3:
        for i in rotMatrix:
            i.append(0)
        rotMatrix.append([0, 0, 1])
    return dot(mat, rotMatrix)

def translate(mat: list, x, y, z = 0):
    for xMat in mat:
        xMat[0] += x
        xMat[1] += y
        if xMat.__len__() == 3: xMat[2] += z
    return mat

def translateMultiplication(mat: list, x, y, z = 0):
    retMatrix = []
    for i in mat:
        i.append(1)
        retMatrix.append(i)
    translateMatrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1]
    ]
    retMatrix = dot(retMatrix, translateMatrix)
    for i in retMatrix:
        for j in i:
            j = j[:-1]
    return retMatrix

def scale(mat: list, x, y, z = 0):
    scaleMatrix = [
        [x, 0],
        [0, y]
    ]
    if mat[0].__len__() == 3:
        for i in scaleMatrix:
            i.append(0)
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
        [2, 0, 1],
        [0, 2, 1]
    ]

    print("Dot product")
    mat = dot(matTwo, matThree)
    for m in mat:
        for n in m:
            print(n)
        print("\n")

    print("Scale")
    scl = scale(matThree, 2, 2)
    for m in scl:
        for n in m:
            print(n)
        print("\n")

    # print("Shear")
    # shr = shear(matThree, x = 2)
    # for m in shr:
    #     for n in m:
    #         print(n)
    #     print("\n")

    print("Transpose")
    trn = transpose(matThree)
    for m in trn:
        print(m)
    print("\n")

    print("Rotation")
    rot = rotation(matThree, 180)
    for m in rot:
        for n in m:
            print(n)
    print("\n")

    print("Translate")
    tsl = translate(matTwo, 2, 2)
    for m in tsl:
        print(m)
    print("\n")

    print("Translate Multiplication")
    tsl = translateMultiplication(matThree, 2, 2)
    for m in tsl:
        for n in m:
            print(n)
    print("\n")
