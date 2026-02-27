# **1. A Note on Matrix Multiplication**

Your Name

## **1.1. Motivation**

Matrix multiplication is a fundamental operation used to describe and compute linear relationships between quantities. It appears throughout science and technology: in physics to model coordinate transformations, in computer graphics to move and project objects in space, in data science and machine learning to apply linear models, and in engineering to represent interconnected systems.

By organizing numbers into matrices, complex systems of equations can be written compactly and evaluated efficiently. Matrix multiplication provides the rule for combining these systems into a single transformation.

### **1.2. Definition**

Matrix multiplication combines rows of one matrix with columns of another. Inline:

$$(AB)_{i,j} = \sum_{k=1}^n A_{i,k} B_{k,j}$$

.

# **1.3. Worked example**

Let

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$$

and

$$B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

.

$$AB = \begin{pmatrix} 1*5 + 2*7 & 1*6 + 2*8 \\ 3*5 + 4*7 & 3*6 + 4*8 \end{pmatrix}$$
$$= \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

#### **1.4. Determinant of a matrix**

The determinant is a scalar value associated with a square matrix. It measures how the matrix scales area or volume and whether the associated linear transformation is invertible. A matrix has an inverse if and only if its determinant is nonzero.

For a 2 times 2 matrix

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

, the determinant is defined as follows.

$$\det(A) = ad - bc$$

### **1.5. Determinant example**

Using the matrix

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$$

, we compute

$$\det(A) = 1 * 4 - 2 * 3$$
$$= -2$$

Since

$$\det(A) \neq 0$$

, the matrix

is invertible.

## **1.6. General definition**

For an × matrix , the determinant is defined as a sum over all permutations of the column indices. Each term selects exactly one entry from each row and each column, multiplied by a sign that depends on the permutation.

$$\det(A) = \sum_{s \in S_n} \operatorname{sgn}(s) \operatorname{prod}_{i=1}^n A_{i,s(i)}$$

Here denotes the set of all permutations of the numbers 1 through , and sgn() is 1 for even permutations and −1 for odd ones.

#### **1.7. Application to quantum mechanics**

In quantum mechanics, physical observables are represented by linear operators acting on a vector space of states. When a basis of states is fixed, these operators can be written as matrices, and the states themselves become vectors.

One of the most important operators is the Hamiltonian, which represents the total energy of the system. Its matrix form determines both the measurable energy levels and the time evolution of quantum states.

If is the Hamiltonian matrix and is a state vector, the stationary states satisfy the eigenvalue equation

$$Hv = Ev$$

where is the energy associated with the state .

In this representation, matrix multiplication encodes how the Hamiltonian acts on a state. The allowed energy levels of the system are obtained by solving the characteristic equation

$$\det(H - EI) = 0$$

where is the identity matrix. This shows how determinants and matrix multiplication together play a central role in quantum theory.