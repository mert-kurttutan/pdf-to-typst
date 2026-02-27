= 1. A Note on Matrix Multiplication

#align(center)[Your Name]

== 1.1. Motivation

Matrix multiplication is a fundamental operation used to describe and compute linear relationships between quantities. It appears throughout science and technology: in physics to model coordinate transformations, in computer graphics to move and project objects in space, in data science and machine learning to apply linear models, and in engineering to represent interconnected systems.

By organizing numbers into matrices, complex systems of equations can be written compactly and evaluated efficiently. Matrix multiplication provides the rule for combining these systems into a single transformation.

=== 1.2. Definition

Matrix multiplication combines rows of one matrix with columns of another. Inline:

$
(A B)_(i, j) = sum_(k=1)^n A_(i, k) B_(k, j)
$

== 1.3. Worked example

Let

$
A = mat(1, 2; 3, 4)
$

and

$
B = mat(5, 6; 7, 8)
$

$
A B = mat(1 dot 5 + 2 dot 7, 1 dot 6 + 2 dot 8; 3 dot 5 + 4 dot 7, 3 dot 6 + 4 dot 8)
$

$
= mat(19, 22; 43, 50)
$

=== 1.4. Determinant of a matrix

The determinant is a scalar value associated with a square matrix. It measures how the matrix scales area or volume and whether the associated linear transformation is invertible. A matrix has an inverse if and only if its determinant is nonzero.

For a $2 times 2$ matrix

$
A = mat(a, b; c, d)
$

the determinant is defined as follows.

$
"det"(A) = a d - b c
$

== 1.5. Determinant example

Using the matrix

$
A = mat(1, 2; 3, 4)
$

we compute

$
"det"(A) = 1 dot 4 - 2 dot 3
$

$
= -2
$

Since

$
"det"(A) != 0
$

the matrix is invertible.

== 1.6. General definition

For an $n times n$ matrix $A$, the determinant is defined as a sum over all permutations of the column indices. Each term selects exactly one entry from each row and each column, multiplied by a sign that depends on the permutation.

$
"det"(A) = sum_(s in S_n) "sgn"(s) product_(i=1)^n A_(i, s(i))
$

Here $S_n$ denotes the set of all permutations of the numbers $1$ through $n$, and $"sgn"(s)$ is $1$ for even permutations and $-1$ for odd ones.

=== 1.7. Application to quantum mechanics

In quantum mechanics, physical observables are represented by linear operators acting on a vector space of states. When a basis of states is fixed, these operators can be written as matrices, and the states themselves become vectors.

One of the most important operators is the Hamiltonian, which represents the total energy of the system. Its matrix form determines both the measurable energy levels and the time evolution of quantum states.

If $H$ is the Hamiltonian matrix and $v$ is a state vector, the stationary states satisfy the eigenvalue equation

$
H v = E v
$

where $E$ is the energy associated with the state $v$.

In this representation, matrix multiplication encodes how the Hamiltonian acts on a state. The allowed energy levels of the system are obtained by solving the characteristic equation

$
"det"(H - E I) = 0
$

where $I$ is the identity matrix. This shows how determinants and matrix multiplication together play a central role in quantum theory.
