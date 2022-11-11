#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    data = {}
    for line in open('Transaction.txt','r'):
        (UserID, TransID, Description, Amount, x, y, fraud) = line.split(':')
        data.setdefault(UserID,{})
        data[UserID][TransID] = str(Description),float(Amount),float(x),float(y),str(fraud)
except FileNotFoundError:
        print(f'File error: Please check if "Transaction.txt" is available in your current working directory.')