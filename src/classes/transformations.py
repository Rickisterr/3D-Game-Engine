import numpy as np

"""
All matrices and equations required throughout the program's calculations
These are imported to the other files for matrix reuse
"""

def RotationMatrix_x(theta):
    
    return np.array([
        [ 1, 0, 0, 0 ],
        [ 0, np.cos(theta), -np.sin(theta), 0 ],
        [ 0, np.sin(theta), np.cos(theta), 0 ],
        [ 0, 0, 0, 1 ]
    ])

    
def RotationMatrix_y(theta):
    
    return np.array([
        [ np.cos(theta), 0, np.sin(theta), 0 ],
        [ 0, 1, 0, 0 ],
        [ -np.sin(theta), 0, np.cos(theta), 0 ],
        [ 0, 0, 0, 1 ]
    ])


def RotationMatrix_z(theta):
    
    return np.array([
        [ np.cos(theta), -np.sin(theta), 0, 0 ],
        [ np.sin(theta), np.cos(theta), 0, 0 ],
        [ 0, 0, 1, 0 ],
        [ 0, 0, 0, 1 ]
    ])


def TranslateMatrix(d_posn):
    
    return np.array([
        [ 1, 0, 0, 0 ],
        [ 0, 1, 0, 0 ],
        [ 0, 0, 1, 0 ],
        [ d_posn[0], d_posn[1], d_posn[2], 1 ]
    ])
    

def ProjectionMatrix():
    
    return np.array([
        [ 1, 0, 0 ],
        [ 0, 1, 0 ],
        [ 0, 0, 0 ]
    ])