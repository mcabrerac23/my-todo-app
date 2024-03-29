import streamlit as st
import pandas
import base64

st.set_page_config(layout="wide")

col1, = st.columns(1)

with col1:
    file_ = open("images/principal_stitch_animated.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )
    st.title("IMPORTACION productos Disney-STITCH")
    content = """Productos STITCH - 2024
    """
    st.info(content)

df = pandas.read_csv("LIM_STORE_2024.csv", sep=",")

col2, col3, col4 = st.columns(3)

col2, empty_col, col3, empty_col, col4 = \
    st.columns([3.5, 0.5, 3.5, 0.5, 3.5])

with col2:
    for index, row in df[:8].iterrows():
        st.header(row["Descripcion de Producto"])
        st.subheader(f'Code: :blue[{row["Codigo Producto"]}]')
        st.write(f'Precio: :red[{row["Precio de Venta SOLES"]}]')
        st.write(f'Stock Disponible: {int(row["Stock Disponible"])}')
        st.image("images/" + row["image"])
        # st.write(f"[Source Code]({row['url']})")

with col3:
    for index, row in df[8:16].iterrows():
        st.header(row["Descripcion de Producto"])
        st.subheader(f'Code: :blue[{row["Codigo Producto"]}]')
        st.write(f'Precio: :red[{row["Precio de Venta SOLES"]}]')
        st.write(f'Stock Disponible: {int(row["Stock Disponible"])}')
        st.image("images/" + row["image"])

with col4:
    for index, row in df[16:24].iterrows():
        st.header(row["Descripcion de Producto"])
        st.subheader(f'Code: :blue[{row["Codigo Producto"]}]')
        st.write(f'Precio: :red[{row["Precio de Venta SOLES"]}]')
        st.write(f'Stock Disponible: {int(row["Stock Disponible"])}')
        st.image("images/" + row["image"])

