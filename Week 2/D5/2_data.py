import streamlit as st

import pandas as pd
import numpy as np

a = [1,2,3,4]
n = np.array(a)

# nd = n.shape(2,4)

dic = {'name':'XXX',
       'age': '18+',
        'country': 'India' }

data = pd.read_csv("data.csv")

st.write(a)
st.write(n)


st.dataframe(data)
st.json(dic)
st.write(data)
st.table(data)
