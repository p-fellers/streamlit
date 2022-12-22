import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import t

hide = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body {overflow: hidden;}
    div.block-container {padding-top:1rem;}
    div.block-container {padding-bottom:1rem;}
    </style>
    """

st.markdown(hide, unsafe_allow_html=True)

col1, col2 = st.columns([2,3])

with col1:
    st.write('Normal Distribution')
    meanmu = st.number_input(
        "Mean",
        value=0.0,
        step=0.1,
        key=11
    )
    stsigma = st.number_input(
        "Standard deviation",
        min_value=0.00,
        value=1.00,
        step=0.01,
        key=12    
    )

    check = st.checkbox("Calculate Probability")

    if check:
        probability = st.selectbox(
            "Probability",
            [
                "P(X < value)",
                "P(X > value)",
                "P(value1 < X < value2)"
            ]
        )
        if probability == "P(value1 < X < value2)":
            value1 = st.number_input(
                "value1",
                value=0.00,
                step=0.01,
                key=21
            )
            value2 = st.number_input(
                "value2",
                value=0.00,
                step=0.01,
                key=21
            )
            
        else:
            value = st.number_input(
                "value",
                value=0.00,
                step=0.01,
                key=21
            )

with col2:
    
    fig, ax = plt.subplots()
    x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
    ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), alpha=0.5)
    ax.set(xlabel='X', ylabel='Density')
    title1=('normal(%0.2f, %0.2f)' %(meanmu, stsigma))

    st.pyplot(fig)
    
