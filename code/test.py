
# %%

# Loading data
import pickle                                       # Data is pickle loaded
import numpy as np                                  # Numpy for pickle


# %% [markdown]
# # Import Data

# %%
Y_train_np = pickle.load(open('/workspace/data/X_train', 'rb')) 

# %%

print(Y_train_np.mean(), Y_train_np.std())
