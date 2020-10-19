import numpy as np

def power_iteration(A, num_simulations: int):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.array([1,.3,0])
    f=open('ouput.tex','w')
    i=0
    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        print(b_k1)
        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        print(b_k1_norm)
        # re normalize the vector
        g=r'{} & $\begin[pmatrix] {:.4f}\\{:.4f}\\{:.4f}\end[pmatrix]$ & {:.4f}\\'.format(i,b_k[0],b_k[1],b_k[2],b_k1_norm)
        g=g.replace('[','{').replace(']','}')
        f.write(g)
        b_k = b_k1 / b_k1_norm

        i+=1
    f.close()
    return b_k
b=[[7, 0,3], [2, 1,1],[2,0,2]]
a=power_iteration(np.array(b), 5)