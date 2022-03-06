import streamlit as st

st.title("Hello")

st.header("Header")
st.subheader("Sub Header")

st.text("Text")

st.markdown("""# H1
## H2
### H3

:moon:

<br>

**BOLD**

__ITALICS__

text""", True)

st.latex(r'''Hyp^2 = Opp_Side^2 + Adj_Side^2''')

st.write("I", "am", "learning")

a = {'key':'value', 'lock':'key'}
st.write(a)



