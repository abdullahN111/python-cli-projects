import streamlit as st

def app():
    
    def convert_units(unit, unit_from, unit_to):
        
        conversions = {
            "meter_kilometer": 0.001,
            "kilometer_meter": 1000,
            "gram_kilogram": 0.001,
            "kilogram_gram": 1000,
            "inch_centimeter": 2.54,
            "centimeter_inch": 0.393701,
        }

        key = f"{unit_from}_{unit_to}"
        
        if key in conversions:
            conversion = conversions[key]
            return value * conversion
        
        else:
            print("Conversion not supported.")


    # st.set_page_config(page_title="iSolutions | Unit Converter", page_icon="⚙")

    st.title("Unit Converter")

    value = st.number_input("Enter the value to convert:")
    unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram", "inch", "centimeter"] )
    unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram", "inch", "centimeter"] )

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write(f"Converted Value: {result}")