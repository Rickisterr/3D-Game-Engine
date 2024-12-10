import numpy as np
import pygame

FRAME_DELAY = 0.001     # delta_t = 1 ms between frames for force calculations

class Object:
    
    def __init__(self, posn, mass, radius):
        self.mass = mass
        self.radius = radius
        self.orientation = np.array([[0, 0, 0]])    # orientation of object as theta_x, theta_y, theta_z
        self.posn = np.array([posn])                # x, y, z components
        self.velocity = np.array([[0, 0, 0]])       # x, y, z components
        self.acceleration = np.array([[0, 0, 0]])   # x, y, z components
        self.id = ""
        self.color = 'white'
        
        
    def setId(self, name, color):
        self.id = name
        self.color = color
    
    
    def rotateObject(self, diff_theta):
        theta = 0
        
        # Rotation over x-axis
        if(diff_theta[0] != 0):
            
            theta = diff_theta[0]
            c = np.cos(theta)
            s = np.sin(theta)
            
            RotationMatrix = np.array( [[ 1, 0, 0 ], 
                                        [ 0, c, -s ], 
                                        [ 0, s, c ]] )
            
            # Rotation operation being performed
            self.posn = np.array(np.round(np.dot(RotationMatrix, self.posn.transpose()), decimals=3)).transpose()
            
        
        # Rotation over y-axis
        if(diff_theta[1] != 0):
            
            theta = diff_theta[1]
            c = np.cos(theta)
            s = np.sin(theta)
            
            RotationMatrix = np.array( [[ c, 0, s ], 
                                        [ 0, 1, 0 ], 
                                        [ -s, 0, c ]] )
            
            # Rotation operation being performed
            self.posn = np.array(np.round(np.dot(RotationMatrix, self.posn.transpose()), decimals=3)).transpose()
            
        
        # Rotation over z-axis
        if(diff_theta[2] != 0):
            
            theta = diff_theta[2]
            c = np.cos(theta)
            s = np.sin(theta)
            
            RotationMatrix = np.array( [[ c, -s, 0 ], 
                                        [ s, c, 0 ],
                                        [ 0, 0, 1 ]] )
        
            # Rotation operation being performed
            self.posn = np.array(np.round(np.dot(RotationMatrix, self.posn.transpose()), decimals=3)).transpose()
        
        # Projecting to 2d after transformation
        self._projectObject()
            
    
    def _projectObject(self):
        
        # Projection matrix for 3d to 2d
        ProjectionMatrix = np.array( [[1, 0, 0],
                                      [0, 1, 0],
                                      [0, 0, 0]] )
        
        # Multiplying position with projection matrix
        self.posn = np.array(np.round(np.dot(ProjectionMatrix, self.posn.transpose()), decimals=3)).transpose()


def testing():
    camera = Object([0, 3, 1], 0, 0)
    
    camera.rotateObject([3*np.pi, 0, 0])
    
    print(camera.posn)
    
    
# def main():
#     camera = Object([0, 0, 0], 10, 10)
    
#     camera.rotateObject


if __name__ == '__main__':
    testing()