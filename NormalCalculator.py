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
    calculate = st.selectbox(
        "Calculate",
        [
            "no calculation",
            "Probability given value",
            "Value given probability"
        ]
        )

    if calculate == "Probability given value":
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
                key=22
            )
            
        else:
            value1 = st.number_input(
                "value",
                value=0.00,
                step=0.01,
                key=23
            )

with col2:
    if calculate == "Probability given value":
        fig, ax = plt.subplots()
        if probability == "P(X < value)":
            x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
            ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), color='tab:blue')
            ax.set(xlabel='X', ylabel='Density')
            title1=('normal(%0.2f, %0.2f)' %(meanmu, stsigma))
            ax.title.set_text(title1)
            st.pyplot(fig)        
            x2 = np.linspace(norm.ppf(0.0001, meanmu, stsigma), value1, 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, norm.pdf(value1, loc=meanmu, scale=stsigma)+.1), scaley = False, color='tab:orange')
        elif probability == "P(X > value)":
            x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
            ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), color='tab:blue')
            ax.set(xlabel='X', ylabel='Density')
            title1=('normal(%0.2f, %0.2f)' %(meanmu, stsigma))
            ax.title.set_text(title1)
            st.pyplot(fig)        
            x2 = np.linspace(value1, norm.ppf(0.9999, meanmu, stsigma), 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, norm.pdf(value1, loc=meanmu, scale=stsigma)+.1), scaley = False, color='tab:orange')
        else:
            x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
            ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), color='tab:blue')
            ax.set(xlabel='X', ylabel='Density')
            title1=('normal(%0.2f, %0.2f)' %(meanmu, stsigma))
            ax.title.set_text(title1)
            st.pyplot(fig)        
            x2 = np.linspace(value1, value2, 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, norm.pdf(value1, loc=meanmu, scale=stsigma)+.1), scaley = False, color='tab:orange')
            ax.plot((value2, value2), (-.02, norm.pdf(value2, loc=meanmu, scale=stsigma)+.1), scaley = False, color='tab:orange')
    else:
        fig, ax = plt.subplots()
        x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
        ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), color='tab:blue')
        ax.set(xlabel='X', ylabel='Density')
        title1=('normal(%0.2f, %0.2f)' %(meanmu, stsigma))
        ax.title.set_text(title1)
    st.pyplot(fig)
    
