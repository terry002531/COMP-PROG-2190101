import numpy as np

def sum_2_rows(M):
    return M[::2,:]+M[1::2,:]

def sum_left_right(M):
    mid = len(M)//2
    w1 = M[:,:mid]
    w2 = M[:,mid:]
    return w1 + w2

def sum_upper_lower(M):
    mid = len(M)//2
    qian = M[:mid,:]
    hou = M[mid:,:]
    return qian + hou

def sum_4_quadrants(M):
    mid = len(M)//2
    q1 = M[:mid,:]
    q2 = M[mid:,:]
    q11 = q1[:,:mid]
    q12 = q1[:,mid:]
    q21 = q2[:,:mid]
    q22 = q2[:,mid:]
    return q11 + q12 + q21 + q22

def sum_4_cells(M):
    q11 = M[::2,::2]
    q12 = M[1::2,::2]
    q21 = M[::2,1::2]
    q22 = M[1::2,1::2]
    return q11 + q12 + q21 + q22

def count_leap_years(years):
    years = years - 543
    n = 0
    for i in years:
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            n += 1
    return n

exec(input().strip())