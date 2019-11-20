#Exercicio RNA - Resolução das matrizes da lista de exercicio 2

#Exercicio "a"
import tensorflow as tf

x1 = tf.constant([[1,0],[2,1]])
x2 = tf.constant([[0,2],[6,1]])

teste = 2 * x1
teste2 = 3 * x2

print(teste)
print(teste2)

soma = teste + teste2
print(soma)

#Exercicio "b"
#não é possivel realizar a operação

#Exercicio "c"
#não é possivel realizar a operação

#Exercicio "d"

d1 = tf.constant([[1,0,2]])
d2 = tf.constant([[2],[3],[1]])

multiD = tf.matmul(d1,d2)
print(multiD)

#Exercicio "e"

e1 = tf.constant([[1,0],[0,0]])
e2 = tf.constant([[0,1],[1,0]])

multiE = tf.matmul(e1,e2)
print(multiE)

#Exercicio "f"

f1 = tf.constant([[0,1],[1,0]])
f2 = tf.constant([[1,0],[0,0]])

multiF = tf.matmul(f1,f2)
print(multiF)

#Exercicio "g"

g1 = tf.constant([[1,2],[3,1],[0,3]])
g2 = tf.constant([[1,0,1],[2,1,0]])

multiG = tf.matmul(g1,g2)
print(multiG)

#Exercicio "h"

h1 = tf.constant([[1,2,0],[3,1,1]])
h2 = tf.constant([[1,0,1],[0,1,0],[1,0,1]])

multiH = tf.matmul(h1,h2)
print(multiH)


#Exercicio "i"

i1 = tf.constant([[1,0,0],[0,1,0],[0,0,1]])
i2 = tf.constant([[30,4],[2,10],[2,20]])

multiI = tf.matmul(i1,i2)
print(multiI)

#Exercicio "j"

j1 = tf.constant([[0,0,1],[0,1,0],[1,0,0]])
j2 = tf.constant([[30,4],[2,10],[2,20]])

multiJ = tf.matmul(j1,j2)
print(multiJ)

#Exercicio "k"

k1 = tf.constant([[1,0,0],[0,1,0],[0,0,3]])
k2 = tf.constant([[30,4],[2,10],[2,20]])

multiK = tf.matmul(k1,k2)
print(multiK)

#Exercicio "l"

l1 = tf.constant([[1,0,0],[0,1,0],[2,0,1]])
l2 = tf.constant([[30,4],[2,10],[2,20]])

multiL = tf.matmul(l1,l2)
print(multiL)
