import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine="openpyxl")
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue

            file_size = file.getbuffer().nbytes / 1024  
            st.write(f"**File Name:** {file.name}")
            st.write(f"**File Size:** {file_size:.2f} KB")

            st.write("Preview of Data:")
            st.dataframe(df.head())

            st.subheader("Data Cleaning Options")
            clean_data = st.checkbox(f"Clean data for {file.name}")

            if clean_data:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")

                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled with column means!")

            st.subheader("Column Selection")
            selected_columns = st.multiselect(f"Choose columns to keep for {file.name}", df.columns, default=df.columns)
            df = df[selected_columns]

            st.subheader("Data Visualization")
            if st.checkbox(f"Show visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2]) 

            st.subheader("Conversion Options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()

                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)

                st.download_button(
                    label=f"Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

        except Exception as e:
            st.error(f"Error processing {file.name}: {str(e)}")

st.success("All files processed!")
