import streamlit as st
import pandas as pd
from io import BytesIO

def app():
    

    # st.set_page_config(page_title="iSolutions | File Converter", layout="wide", page_icon="⚙")

    st.title("File Converter & Cleaner")
    st.write("Upload CSV or Excel file to convert it to another format or clean it.")

    files = st.file_uploader("Upload file", type=["csv", "xlsx"], accept_multiple_files=True)

    if files:
        for file in files:
            extension = file.name.split(".")[-1]

            if file.name not in st.session_state:
                if extension == "csv":
                    df = pd.read_csv(file)
                else:
                    df = pd.read_excel(file)
                st.session_state[f"df_{file.name}"] = df

            df = st.session_state[f"df_{file.name}"]

            st.subheader(f"{file.name} - Preview")
            st.dataframe(df.head())

            if st.checkbox(f"Remove duplicates - {file.name}"):
                st.session_state[f"df_{file.name}"] = df.drop_duplicates()
                st.success("Duplicates removed.")
                st.dataframe(st.session_state[f"df_{file.name}"])

            if st.checkbox(f"Fill missing values - {file.name}"):
                st.session_state[f"df_{file.name}"] = df.fillna(df.select_dtypes(include="number").mean())
                st.success("Missing values filled.")
                st.dataframe(st.session_state[f"df_{file.name}"])

            selected_columns = st.multiselect(f"Select columns to keep - {file.name}", df.columns, default=df.columns)
            st.session_state[f"df_{file.name}"] = df[selected_columns]
            st.dataframe(st.session_state[f"df_{file.name}"])

            numeric_df = st.session_state[f"df_{file.name}"].select_dtypes(include="number")
            if st.checkbox(f"Show chart - {file.name}") and not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :2])

            format_choice = st.radio(f"Select format to convert - {file.name}", ["csv", "xlsx"], key=file.name)

            if st.button(f"Download {file.name} as {format_choice}"):
                output = BytesIO()
                new_name = f"{file.name.rsplit('.', 1)[0]}.{format_choice}"
                
                if format_choice == "csv":
                    st.session_state[f"df_{file.name}"].to_csv(output, index=False)
                    mime_type = "text/csv"
                else:
                    with pd.ExcelWriter(output, engine="openpyxl") as writer:
                        st.session_state[f"df_{file.name}"].to_excel(writer, index=False)
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                output.seek(0)
                st.download_button(label=f"Download {new_name}", data=output, file_name=new_name, mime=mime_type)
                st.success(f"{file.name} converted to {format_choice} successfully.")
