#%%
import numpy as np
#%%
mylist = [1,2,3]
type(mylist)
#%%
arr = np.array(mylist)
arr
type(arr)
#%%
np.arange(0,10)
#%%
np.arange(0,10,.2)
# %%
np.zeros(shape=(10,5))
# %%
np.ones(shape=(10,5))





# %%
# linspace
np.random.seed(101)
arr = np.random.randint(0,100,10)
print("arr =", arr)

arr2 = np.random.randint(0,100,10)
print("arr2 =", arr2)
# %%
print("arr.max() =", arr.max())
print("arr.argmax() =", arr.argmax())
print("arr.min() =", arr.min())
print("arr.argmin() =", arr.argmin())
print("arr.mean() =", arr.mean())
print("arr.shape =", arr.shape)
arr = arr.reshape(2,5)
print("arr.shape =", arr.shape)
# %%
# indexing and slicing
mat = np.arange(0, 100).reshape(10,10)
print("mat =", mat)
print("mat[4,6] =", mat[4,6])
print("mat[:,1] =", mat[:,1])
print("mat[:,1].shape =", mat[:,1].shape)
print("mat[:,1].reshape(10,1) =", mat[:,1].reshape(10,1))
print("mat[5,:] =", mat[5,:])
print("mat[0:3,0:3] =", mat[0:3,0:3])