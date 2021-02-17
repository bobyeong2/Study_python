# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: data-anal
#     language: python
#     name: data-anal
# ---

def Stack():
    
    stack = []
    
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    
    while stack :
        
        print("stack pop value : ", stack.pop())
        


# +

Stack()
# -


