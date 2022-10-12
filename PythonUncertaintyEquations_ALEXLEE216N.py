#!/usr/bin/env python
# coding: utf-8

# ## Python Uncertainty Equations
# ##### Alex Lee PSHX 216N

# # Rule 3

# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$
#         

# In[11]:


# rule 3 equation

import numpy as np

def rule3(dA,dB):
    dQ=np.sqrt(dA**2+dB**2)
    return dQ
dA=1.4
dB=32.1

dQ=rule3(dA,dB)
print("dQ=",dQ)


# In[5]:


x=np.array([1,1.1,1.2,.9,.85])
y=x*3
ysq=y**2
print(ysq)
err_x=np.std(x)/np.sqrt(5)
avgx=np.average(x)
print(avgx,err_x)


# # Rule 4

# # $\frac{\delta Q}{Q}=\sqrt{\frac{(m\delta A)}{A}^2 + \frac{(n\delta B)}{B}^2}$

# In[24]:


theta=np.array([33.0,33.1,32.7,32.8,32.0,33.0,32.6,33.6,33.0,32.8])
print(theta)
avg_theta=np.sum(theta)/len(theta)
print("avg theta:",avg_theta)
err_theta=np.std(x)/np.sqrt(len(theta))
print("error in theta:", err_theta)


# In[43]:


# rule 4 equation

def rule4(A,uncertaintyA,m,B,uncertaintyB,n):
    dQ=np.sqrt( ((m*uncertaintyA)/A) + ((n*uncertaintyB)/B) )
    return dQ
arrayA=np.array([33.0,33.1,32.7,32.8,32.0,33.0,32.6,33.6,33.0,32.8])
arrayB=np.array([33.0,33.1,32.7,32.8,32.0,33.0,32.6,33.6,33.0,32.8])
A=np.sum(arrayA)/len(arrayA)
B=np.sum(arrayB)/len(arrayB)
m=1
n=2
uncertaintyA=3
uncertaintyB=2
dQ=rule4(A,uncertaintyA,m,B,uncertaintyB,n)
print(arrayA)
print(arrayB)
print("dQ=", dQ)
print(rule4(A,uncertaintyA,m,B,uncertaintyB,n))


# # Rule 2

# In[40]:


def rule2(uncertaintyA,A,m):
    val=m*(uncertaintyA/A)
    return val.as_integer_ratio()
q=rule2(.5,2,5)
print(q)
print("Q Uncertainty= ",q[0])
print("Q= ",q[1])


# # Rule 1

# In[42]:


def rule1(c,uncertaintyA):
    dQ=c*uncertaintyA
    return dQ
arrayA=np.array([33.0,33.1,32.7,32.8,32.0,33.0,32.6,33.6,33.0,32.8])
A=np.sum(arrayA)/len(arrayA)
c=1
print(arrayA)
print("dQ=",dQ)


# In[ ]:




