import streamlit as st
import json
import os
from utils import calculate_dosage

# Page Setup
st.set_page_config(page_title="Clinical Assist AI", layout="centered")

def load_data():
    with open('data/drugs.json', 'r') as f:
        return json.load(f)['drugs']

st.title("🚨 Clinical Assist AI")
st.markdown("---")

# Inputs
data = load_data()
categories = list(set([d['category'] for d in data]))
selected_cat = st.sidebar.selectbox("Select Scenario", categories)
weight = st.sidebar.number_input("Patient Weight (kg)", min_value=1.0, value=70.0)

# Filter
filtered = [d for d in data if d['category'] == selected_cat]

for drug in filtered:
    dose, is_alert = calculate_dosage(drug, weight)
    
    with st.container(border=True):
        st.subheader(drug['name'])
        
        # Display Dose
        st.metric("Calculated Dose", f"{dose} {drug['unit']}")
        
        # Display Prep
        st.info(f"**Preparation:** {drug['prep']}")
        
        # Safety Alert
        if is_alert:
            st.error(f"⚠️ SAFETY: Dose exceeds standard max ({drug['max_dose']}{drug['unit']})")
        else:
            st.warning(f"**Alert:** {drug['safety_alert']}")

st.sidebar.caption("DISCLAIMER: Always verify before administration.")