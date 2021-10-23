# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Implementing Hash Table in Python

# %%
def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


