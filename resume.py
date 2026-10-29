import streamlit as st

st.set_page_config(page_title="Sheilyn Colina | Data Science", layout="centered")
st.title("Sheilyn Colina")
st.subheader("Ciencia de Datos · Finanzas Cuantitativas")
st.write("Estudiante de Ciencia de Datos en Universitat Carlemany. Desarrollo proyectos de análisis de datos e investigación cuantitativa en Python y SQL.")
st.header("Formación")
st.write("Grado en Ciencia de Datos — Universitat Carlemany, en curso; finalización prevista en 2027.")
st.header("Proyectos")
for title, url, detail in [
    ("IBKR Portfolio Analytics", "https://github.com/sheicol/ibkr-quant-portfolio-analysis", "Composición, concentración y actividad de trading con SQL y Python. En desarrollo."),
    ("Calidad del aire", "https://github.com/sheicol/analisis-calidad-aire-medellin", "Análisis exploratorio con datos abiertos y Python."),
    ("SheyQuant Research Lab", "https://github.com/sheicol/quant-research-portfolio", "Investigación de portafolios por objetivos; implementación pendiente."),
]:
    st.markdown(f"### [{title}]({url})")
    st.write(detail)
st.header("Herramientas aplicadas")
st.write("Python, pandas, visualización de datos, SQL, PostgreSQL y KNIME. Consulta cada proyecto para ver su alcance y estado.")
st.markdown("[GitHub](https://github.com/sheicol) · [LinkedIn](https://www.linkedin.com/in/sheilyn-colina-54b09097/)")
