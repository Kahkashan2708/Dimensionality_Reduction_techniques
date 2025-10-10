# Scatter Plot code- Before and after LDA

plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
for label, color in zip(np.unique(y_train), ['red', 'green', 'blue']):
    plt.scatter(X_train[y_train==label, 0],
                X_train[y_train==label, 1],
                label=iris.target_names[label],
                alpha=0.7, color=color)
plt.xlabel('Feature 1 (Sepal Length)')
plt.ylabel('Feature 2 (Sepal Width)')
plt.title('Original Data (Before LDA)')
plt.legend()

# -------- Plot 2: LDA projection --------
plt.subplot(1,2,2)
for label, color in zip(np.unique(y_train), ['red', 'green', 'blue']):
    plt.scatter(X_train_lda[y_train==label, 0],
                X_train_lda[y_train==label, 1],
                label=iris.target_names[label],
                alpha=0.7, color=color)
plt.xlabel('Linear Discriminant 1')
plt.ylabel('Linear Discriminant 2')
plt.title('After LDA Projection')
plt.legend()

plt.tight_layout()
plt.show()
