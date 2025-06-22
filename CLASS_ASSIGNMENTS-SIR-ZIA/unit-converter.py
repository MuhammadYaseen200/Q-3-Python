import streamlit as st

# Title of the app
st.title("Unit Converter")

# Define conversion factors for each category (base unit factors)
units = {
    'Length': {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254,
    },
    'Mass': {
        'kilograms': 1,
        'grams': 0.001,
        'milligrams': 0.000001,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'tons': 1000,  # metric tons
    },
    'Volume': {
        'liters': 1,
        'milliliters': 0.001,
        'cubic meters': 1000,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.24,
    },
    'Pressure': {
        'Pascals (Pa)': 1,
        'bar': 1e5,
        'atmospheres': 101325,
        'psi': 6894.76,
        'torr': 133.322,
    },
    'Time': {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'years': 31536000,
    },
    'Data': {
        'bits': 1,
        'bytes': 8,
        'kilobits': 1000,
        'kilobytes': 8000,
        'megabits': 1e6,
        'megabytes': 8e6,
        'gigabits': 1e9,
        'gigabytes': 8e9,
    },
    'Energy': {
        'Joules': 1,
        'kilojoules': 1000,
        'calories': 4.184,
        'kilocalories': 4184,
        'watt-hours': 3600,
        'kilowatt-hours': 3.6e6,
        'BTU': 1055.06,
    },
    'Speed': {
        'm/s': 1,
        'km/h': 0.277778,
        'mph': 0.44704,
        'ft/s': 0.3048,
        'knots': 0.514444,
    },
    'Area': {
        'square meters': 1,
        'square kilometers': 1e6,
        'square feet': 0.092903,
        'square inches': 0.00064516,
        'acres': 4046.86,
        'hectares': 10000,
    },
    'Angle': {
        'degrees': 0.0174533,   # radians per degree
        'radians': 1,
        'gradians': 0.0157079,  # radians per gradian
    },
}

# Temperature units (handled separately because of offset formulas)
temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

# Let user select a category
category = st.selectbox("Select category", list(units.keys()) + ["Temperature"])

# Determine the available units for 'from' and 'to'
if category != "Temperature":
    unit_dict = units[category]
    options = list(unit_dict.keys())
else:
    options = temp_units

# Select boxes for choosing units
from_unit = st.selectbox("From unit", options)
to_unit = st.selectbox("To unit", options)

# Input field for the numeric value to convert
value_str = st.text_input("Enter value to convert", "")

# Button to trigger the conversion
if st.button("Convert"):
    # Validate that the input is numeric
    try:
        value = float(value_str)
    except:
        st.error("Please enter a numeric value.")
    else:
        # Handle Temperature conversions separately (offset formulas)
        if category == "Temperature":
            if from_unit == to_unit:
                # No conversion needed if units are the same
                result = value
                formula = f"{value}"
            else:
                # Convert input to Celsius as an intermediate
                if from_unit == "Celsius":
                    c = value
                elif from_unit == "Fahrenheit":
                    c = (value - 32) * 5/9
                elif from_unit == "Kelvin":
                    c = value - 273.15
                # Now convert from Celsius to the target unit
                if to_unit == "Celsius":
                    result = c
                    formula = f"{value} (input) -> {c:.2f} °C"
                elif to_unit == "Fahrenheit":
                    result = c * 9/5 + 32
                    formula = f"{value} (input) -> {c:.2f} °C -> {result:.2f} °F"
                elif to_unit == "Kelvin":
                    result = c + 273.15
                    formula = f"{value} (input) -> {c:.2f} °C -> {result:.2f} K"
        else:
            # Non-temperature categories (simple multiply/divide by factors)
            if from_unit == to_unit:
                result = value
                formula = f"{value}"
            else:
                # Convert to base unit, then to target unit
                base_val = value * unit_dict[from_unit]
                result = base_val / unit_dict[to_unit]
                formula = f"{value} × {unit_dict[from_unit]} ÷ {unit_dict[to_unit]} = {result}"
        # Display the result and the formula
        st.write(f"**Result:** {value} {from_unit} = {result} {to_unit}")
        st.write(f"**Calculation:** {formula}")
