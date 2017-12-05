import numpy as np
def poisEvent(lambdax,nx):
    return np.exp(-lambdax)

if __name__ == '__main__':
    print(poisEvent(2,2))