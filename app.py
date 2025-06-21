import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="💊 Medicine Info Finder", page_icon="🩺", layout="centered")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("MedicInfo.csv")

df = load_data()

# Title and description
st.title("💊 Intelligent Medicine Finder")
st.markdown("""
Type the **exact or partial name** of a medicine (e.g., `Azithral 500 Tablet`)  
and get all available details like price, composition, manufacturer, etc.
""")

# User input
medicine_input = st.text_input("🔍 Enter medicine name", "")

# Process
if st.button("Get Info"):
    if not medicine_input.strip():
        st.warning("Please enter a medicine name.")
    else:
        matches = df[df['name'].str.contains(medicine_input, case=False, na=False)]
        if matches.empty:
            st.error("❌ No matching medicine found.")
        else:
            st.success(f"✅ Found {len(matches)} matching result(s).")
            for i, row in matches.iterrows():
                st.markdown("---")
                st.markdown(f"### 💊 **{row['name']}**")
                st.markdown(f"- **Price**: ₹{row['price(₹)']}")
                st.markdown(f"- **Manufacturer**: {row['manufacturer_name']}")
                st.markdown(f"- **Pack Size**: {row['pack_size_label']}")
                st.markdown(f"- **Type**: {row['type']}")
                st.markdown(f"- **Composition 1**: {row['short_composition1']}")
                st.markdown(f"- **Composition 2**: {row['short_composition2']}")
                st.markdown(f"- **Discontinued?**: {'Yes' if row['Is_discontinued'] else 'No'}")

# Sidebar
st.sidebar.title("🧾 About This App")
st.sidebar.info("""
This app retrieves **full medicine details** by name.

- Search by partial or full name
- View manufacturer, price, type, composition, and more

Made with ❤️ by Yash Dev.
""")
