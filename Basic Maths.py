import numpy as np

mat1 = np.array([1, 7, 3, 5, 6, 8, 9, 2, 0]).reshape(3, 3)
print(mat1.ndim)
#gives the number of dimensions

mat2 = np.array([i for i in range(0, 18, 2)]).reshape(3, 3)

mat3 = np.array([i for i in range(6)]).reshape(2, 3)


def add_matrix(A, B):

    resultant = []

    for i in range(len(A)):
        resultant.append(A[i] + B[i])

    return np.array(resultant)


add = add_matrix(mat1, mat2)
#or simply
add = mat1 + mat2

#---------------------------------------------------------------#

dot_prod1 = np.dot(mat1, mat2)
#returns cross product...it's weird, ik
dot_prod2 = np.dot(5, mat2)
#returns element-wise multiplication with scalar


det_mat1 = np.linalg.det(mat1)
trans_mat1 = mat1.T
