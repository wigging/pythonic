---
title: Selectbox widget
date: February 4, 2023
---

Example of a selectbox widget using a callback function and session state.

```python
import streamlit as st


def print_selected():
    print('You have selected: ', st.session_state.selected)


data = ['one', 'two', 'three', 'four']

st.header('Example of a selectbox widget')
st.selectbox('Select at item', data, key='selected', on_change=print_selected)
st.write('You selected: ', st.session_state.selected)
```

<p><img src="../img/streamlit-selectbox.png" style="max-width:100%;" alt="selectbox"></p>
