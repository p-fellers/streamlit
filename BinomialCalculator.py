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
    st.write('Binomial Distribution')
    nobs = st.number_input(
        "n",
        min_value=1,
        step=1,
        value=1,
        key=11
    )
    bprob = st.number_input(
        label="Probability",
        min_value=0.00,
        max_value=1.00,
        value=0.50,
        step=0.01,
        key=12
    )

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
                "P(X = value)",
                "P(X < value)",
                "P(X > value)",
                "P(value1 < X < value2)"
            ]
        )
        if probability == "P(value1 < X < value2)":
            value1 = st.number_input(
                "value1",
                min_value=0,
                max_value=int(nobs)+1,
                step=1,
                value=0,
                key=21
            )
            value2 = st.number_input(
                "value2",
                min_value=0,
                max_value=int(nobs)+1,
                step=1,
                value=1,
                key=22
            )
            
        else:
            value1 = st.number_input(
                "value",
                min_value=0,
                max_value=int(nobs)+1,
                step=1,
                value=1,
                key=23
            )
   
    if calculate == "Value given probability":
        tail = st.selectbox(
            "Location",
            [
                "lower tail",
                "upper tail",
                "middle"
            ]
        )
        prob = st.number_input(
                "prob",
                min_value=0.000,
                max_value=1.000,
                value=0.500,
                step=0.001,
                key = 3.1
        )

with col2:
    if calculate == "Probability given value":
        fig, ax = plt.subplots()
        x = range(0, int(nobs)+1)
        ax.bar(x, height=binom.pmf(k=x, n=nobs, p=bprob), width=0.75, color='tab:blue')
        ax.set(xlabel='X', ylabel='Probability')
        title1=("binomial( %d, %0.2f)" %(nobs, bprob))
        ax.title.set_text(title1)
        plt.ylim(bottom=0)  
        if probability == "P(X < value)":    
            x2 = range(0, int(value1))
            ax.bar(x2, height=binom.pmf(k=x2, n=nobs, p=bprob), width=0.75, color='tab:orange')
            probcalc = binom.cdf(int(value1)-1, n=nobs, p=bprob)
            text="P(X < %d) = %0.3f" %(value1, probcalc) 
        elif probability == "P(X > value)":     
            x2 = range(int(value1)+1, int(nobs)+1)
            ax.bar(x2, height=binom.pmf(k=x2, n=nobs, p=bprob), width=0.75, color='tab:orange')
            probcalc = 1-binom.cdf(value1, n=nobs, p=bprob)
            text="P(X > %d) = %0.3f" %(value1, probcalc)
        elif probability == "P(value1 < X < value2)":     
            x2 = range(int(value1)+1, int(value2))
            y2 = binom.pmf(k=x2, n=nobs, p=bprob)
            ax.bar(x2, height=binom.pmf(k=x2, n=nobs, p=bprob), width=0.75, color='tab:orange')
            probcalc = binom.cdf(int(value2)-1, n=nobs, p=bprob)-binom.cdf(value1, n=nobs, p=bprob)
            text="P(%d < X < %d) = %0.3f" %(value1, value2, probcalc)
        else:
            x2 = int(value1)
            y2 = binom.pmf(k=x2, n=nobs, p=bprob)
            ax.bar(x2, height=binom.pmf(k=x2, n=nobs, p=bprob), width=0.75, color='tab:orange')
            probcalc = binom.pmf(int(value1), n=nobs, p=bprob)
            text="P(X = %d) = %0.3f" %(value1, probcalc)
    elif calculate == "Value given probability":
        fig, ax = plt.subplots()
        x = range(0, int(nobs)+1)
        ax.bar(x, height=binom.pmf(k=x, n=nobs, p=bprob), color='tab:blue')
        ax.set(xlabel='X', ylabel='Probability')
        title1=("binomial( %d, %0.2f)" %(nobs, bprob))
        plt.ylim(bottom=0) 
        ax.title.set_text(title1)
        if tail == "lower tail":
            valresult=binom.ppf(prob, n=nobs, p=bprob)
            x2 = range(0, int(valresult))
            ax.bar(x2, height=binom.pmf(k=x2, n=nobs, p=bprob), color='tab:orange')
            text="P(X < %d) = %0.3f" %(valresult, prob)
        elif tail == "upper tail":
            valresult=binom.ppf((1-prob), n=nobs, p=bprob)
            x2 = range(valresult, int(nobs)+1)
            y2 = binom.pmf(k=x2, n=nobs, p=bprob)
            ax.bar(x2, height=y2, color='tab:orange')
            text="P(X > %d) = %0.3f" %(valresult, prob)
        else:
            valresult1=binom.ppf((1-prob)/2, n=nobs, p=bprob)
            valresult2=binom.ppf(1-(1-prob)/2, n=nobs, p=bprob)
            x2 = range(int(valresult1), int(valresult2))
            y2 = binom.pmf(k=x2, n=nobs, p=bprob)
            ax.bar(x2, height=y2, color='tab:orange')
            text="P(%d < X < %d) = %0.3f" %(valresult1, valresult2, prob)            
    else:
        fig, ax = plt.subplots()
        x = range(0, int(nobs)+1)
        ax.bar(x, height=binom.pmf(k=x, n=nobs, p=bprob), color='tab:blue')
        ax.set(xlabel='X', ylabel='Probability')
        title1=("binomial( %d, %0.2f)" %(nobs, bprob))
        ax.title.set_text(title1)
        plt.ylim(bottom=0) 
        text=""
    st.pyplot(fig)
    st.markdown(f"""<div style='text-align: center'>{text}</h1>""", unsafe_allow_html=True)

