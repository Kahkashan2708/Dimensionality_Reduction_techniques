import numpy as np

def demonstrate_svd(A):
    """
    Performs Singular Value Decomposition (SVD) on a given matrix A,
    prints U, S (singular values), V^T, and reconstructs the matrix.

    Parameters:
        A (numpy.ndarray): Input matrix.

    Returns:
        dict: A dictionary containing U, S, Vt, and reconstructed A.
    """
    # Compute SVD
    U, S, Vt = np.linalg.svd(A)
    
    print("Input Matrix A =\n", A)
    print("\nU =\n", U)
    print("\nSingular Values =", S)
    print("\nV^T =\n", Vt)

    # Build Sigma matrix manually for reconstruction
    Sigma = np.zeros((A.shape[0], A.shape[1]))
    np.fill_diagonal(Sigma, S)

    # Reconstruct A
    A_reconstructed = U @ Sigma @ Vt
    print("\nReconstructed A =\n", A_reconstructed)

    return {
        "U": U,
        "S": S,
        "Vt": Vt,
        "A_reconstructed": A_reconstructed
    }

# Example usage
if __name__ == "__main__":
    A = np.array([[1, 0],
                  [0, 1],
                  [1, 1]])
    demonstrate_svd(A)
