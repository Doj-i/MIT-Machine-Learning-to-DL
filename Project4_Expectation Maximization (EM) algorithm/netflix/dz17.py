import numpy as np
state = [0, 1, 2, 3, 4]
action = [0, 1, 2] #representing moving left, staying, moving right respectively
# transition probability

T = np.array([ [[1/2,1/2,0,0,0], [1/2,1/2,0,0,0], [2/3,1/3,0,0,0]], \
               [[1/3,2/3,0,0,0], [1/4,1/2,1/4,0,0], [0,2/3,1/3,0,0]],\
               [[0,1/3,2/3,0,0], [0,1/4,1/2,1/4,0], [0,0,2/3,1/3,0]], \
               [[0,0,1/3,2/3,0], [0,0,1/4,1/2,1/4], [0,0,0,2/3,1/3]], \
               [[0,0,0,1/3,2/3], [0,0,0,1/2,1/2], [0,0,0,1/2,1/2]], ])

num_state = 5
num_action = 3
r = 1/2
# initialization
V = np.zeros(5)
# reward
R = np.zeros(5)
R[4] = 1
num_iter = 10
for i in range(num_iter):
    Q = [[sum([T[s][a][t] * (R[s] + r * V[t]) for t in range(num_state)]) \
            for a in range(num_action)] for s in range(num_state)]

V = np.max(Q, axis=1)
print(V)

