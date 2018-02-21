
# coding: utf-8

# In[5]:


def compute():
    try:
        print("Inside the try block")
        x = 5 / 0
    except:
        print("Division by zero not possible")


# In[6]:


compute()

