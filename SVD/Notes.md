# SINGULAR VALUE DECOMPOSITION

## 1. What is Singular Value Decomposition (SVD)?

SVD is a method to decompose (factorize) any real matrix \( A \) into three special matrices:

\[
A = U \Sigma V^T
\]

Where:

| Symbol | Meaning | Shape |
|--------|--------|-------|
| \( A \) | Original matrix | \( m \times n \) |
| \( U \) | Left singular vectors (orthogonal) | \( m \times m \) |
| \( \Sigma \) | Diagonal matrix of singular values | \( m \times n \) |
| \( V^T \) | Transpose of right singular vectors | \( n \times n \) |

Singular values are non-negative and ordered:

\[
\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0 \quad \text{where} \quad r = \text{rank}(A)
\]

---

## 2. Mathematical Form

\[
A = U \Sigma V^T
\]

- \( U \): Contains left singular vectors.
- \( \Sigma \): Contains singular values on the diagonal.
- \( V \): Contains right singular vectors.

---

## 3. Geometric Interpretation

Any linear transformation \( A \) can be seen as a sequence of operations:

1. Rotate the input space using \( V \),
2. Stretch or compress along orthogonal axes using \( \Sigma \),
3. Rotate again into the output space using \( U \).

Example: A circle transformed by \( A \) becomes an ellipse.

- Axes directions of the ellipse → columns of \( V \)
- Stretching factors → singular values in \( \Sigma \)
- Final orientation → matrix \( U \)

---

## 4. Connection Between SVD and Eigen Decomposition

If \( A \) is not square, we cannot directly compute eigenvalues. Instead, form:

- \( A^T A \): Square matrix of size \( n \times n \)
- \( A A^T \): Square matrix of size \( m \times m \)

Then:

- Columns of \( V \) are eigenvectors of \( A^T A \)
- Columns of \( U \) are eigenvectors of \( A A^T \)
- Singular values satisfy:

\[
A^T A V = V \Sigma^2 \quad \text{and} \quad A A^T U = U \Sigma^2
\]

---

## 5. Link Between SVD and PCA

PCA finds directions (principal components) where data variance is maximum.

Covariance matrix:

\[
C = \frac{1}{n} X^T X
\]

Perform SVD on centered data \( X \):

\[
X = U \Sigma V^T
\]

Then:

\[
C = \frac{1}{n} V \Sigma^2 V^T
\]

This implies:

- Principal components in PCA = Right singular vectors \( V \)
- Eigenvalues of covariance matrix = \( \frac{\Sigma^2}{n} \)

Therefore:

\[
\text{PCA} = \text{SVD on centered data}
\]

---

## 6. Uses of SVD

| Application | Description |
|-------------|------------|
| PCA | Dimensionality reduction using singular vectors |
| Latent Semantic Analysis (LSA) | Topic extraction in NLP |
| Noise Reduction | Keep top singular values (signal), drop the rest (noise) |
| Image Compression | Approximates image with fewer singular values |
| Recommendation Systems | Matrix factorization for user-item ratings |

---

## 7. Key Properties

- Singular values are non-negative.
- \( U \) and \( V \) are orthogonal matrices.
- Rank of \( A \) equals number of non-zero singular values.
- SVD works for any real (even non-square) matrix.
- Best low-rank approximation property:

\[
A_k = U_k \Sigma_k V_k^T
\]

is the closest rank-\( k \) approximation to \( A \).

---

## 8. Low-Rank Approximation Intuition (Used in PCA)

If only top \( k \) singular values are kept:

\[
A \approx U_k \Sigma_k V_k^T
\]

Then:

- The matrix is compressed.
- Information loss is minimal in least-squares sense.
- This is exactly what PCA does by keeping top \( k \) principal components.

---
