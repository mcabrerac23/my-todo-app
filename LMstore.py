import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, = st.columns(1)

with col1:
    st.image("images/principal_stitch.png", width=300)
    st.title("IMPORTACION productos STITCH")
    content = """Productos STITCH - 2024
    """
    st.info(content)

df = pandas.read_csv("LIM_STORE_2024.csv", sep=",")

col2, col3, col4 = st.columns(3)

col2, empty_col, col3, empty_col, col4 = \
    st.columns([3.5, 0.5, 3.5, 0.5, 3.5])

with col2:
    for index, row in df[:8].iterrows():
        st.header(f'Code: :blue[{row["Codigo Producto"]}]')
        st.subheader(row["Descripcion de Producto"])
        st.write(f'Precio: :red[{row["Precio de Venta SOLES"]}]')
        st.write(f'Stock Disponible: {int(row["Stock Disponible"])}')
        st.image("images/" + row["image"])
        # st.write(f"[Source Code]({row['url']})")

with col3:
    for index, row in df[8:16].iterrows():
        st.header(f'Code: :blue[{row["Codigo Producto"]}]')
        st.subheader(row["Descripcion de Producto"])
        st.write(f'Precio: :red[{row["Precio de Venta SOLES"]}]')
        st.write(f'Stock Disponible: {int(row["Stock Disponible"])}')
        st.image("images/" + row["image"])

with col4:
    for index, row in df[16:24].iterrows():
        st.header(f'Code: :blue[{row["Codigo Producto"]}]')
        st.subheader(row["Descripcion de Producto"])
        st.write(f'Precio: :red[{row["Precio de Venta SOLES"]}]')
        st.write(f'Stock Disponible: {int(row["Stock Disponible"])}')
        st.image("images/" + row["image"])

