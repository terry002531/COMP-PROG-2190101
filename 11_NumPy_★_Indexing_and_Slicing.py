import numpy as np

def get_column_from_bottom_to_top(A , c):
    return A.T[c][::-1]

def get_odd_rows(A):
    return A[1::2,:]

def get_even_column_last_row(A):
    return A[-1,::2]

def get_diagonal1(A):
    return np.diag(A)

def get_diagonal2(A):
    return np.diag(np.rot90(A))

exec(input().strip())