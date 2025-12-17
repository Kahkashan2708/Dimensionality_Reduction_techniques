# Autoencoders

An **Autoencoder (AE)** is an **unsupervised neural network** that learns to **reconstruct its input** by compressing it into a lower-dimensional representation and then decoding it back.

**Core idea:**  
Learn useful features by forcing the network to pass data through a **bottleneck (latent space)**.

---

## 2. Architecture
Input (x) → Encoder → Latent Space (z) → Decoder → Output (x̂)

- **Encoder:** compresses input  
- **Latent space (bottleneck):** compact representation  
- **Decoder:** reconstructs input  

**Mathematical form:**
- Encoder: `z = f(x) = σ(Wₑx + bₑ)`
- Decoder: `x̂ = g(z) = σ(W𝒹z + b𝒹)`
- Goal: `x̂ ≈ x`

---

## 3. Loss Function 
Autoencoders minimize the difference between input and output.

- **Mean Squared Error (MSE):**  
  `L = ||x − x̂||²`
- **Binary Cross-Entropy:** for normalized inputs (0–1)

---

## 4. Training
- Input = Output (x → x)
- Optimized using **backpropagation**
- Optimizers: SGD, Adam
- No labels required

-> Without constraints, AEs may learn the **identity function**

---

## 5. Types of Autoencoders 

### 5.1 Vanilla Autoencoder
- Simple encoder–decoder
- Fully connected layers

### 5.2 Undercomplete Autoencoder
- Latent dimension < input dimension
- Forces meaningful compression

### 5.3 Sparse Autoencoder
- Adds sparsity constraint on latent neurons
- Uses **KL-divergence** penalty

### 5.4 Denoising Autoencoder
- Input is corrupted with noise
- Output is clean input
- Learns robust features

### 5.5 Contractive Autoencoder
- Penalizes sensitivity to input changes
- Improves robustness

### 5.6 Variational Autoencoder (VAE)
- **Probabilistic & generative**
- Encoder outputs mean (μ) and variance (σ²)
- Loss = Reconstruction + KL Divergence
- Used for data generation

### 5.7 Convolutional Autoencoder
- Uses CNN layers
- Best suited for images

---

## 6. Autoencoder vs PCA 

| Feature | PCA | Autoencoder |
|------|-----|------------|
| Nature | Linear | Non-linear |
| Method | Eigen decomposition | Neural network |
| Flexibility | Low | High |
| Reconstruction | Linear | Non-linear |
| Scalability | Limited | High |

**AE ≡ PCA only when:** linear activation + MSE + single hidden layer

---

## 7. Applications
- Dimensionality reduction
- Feature extraction
- Image compression
- Noise removal
- Anomaly detection
- Pretraining deep networks

---

## 8. Autoencoders for Anomaly Detection
- Train on **normal data**
- Anomalies → **high reconstruction error**

Used in fraud detection, fault detection, cybersecurity.

---

## 9. Advantages
- Learns complex non-linear features
- Works well on high-dimensional data
- Flexible architecture

---

## 10. Limitations
- Requires large datasets
- Hard to interpret latent features
- Sensitive to hyperparameters
- Risk of overfitting

---

## One-Line Definitions
- **Encoder:** maps input to latent space  
- **Decoder:** reconstructs input from latent code  
- **Latent space:** compressed feature representation  
- **Reconstruction loss:** measures input–output error  

--- 
