import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_friedman1

hide = """
        &lt;style&gt;
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body {overflow: hidden;}
        div.block-container {padding-top:1rem;}
        div.block-container {padding-bottom:1rem;}
        &lt;/style&gt;
        """

st.markdown(hide, unsafe_allow_html=True)

## Generate simulated data
data = make_friedman1(n_samples=100, n_features=6, noise=3, random_state=1234)

col01, col02 = st.columns([1, 1])

with col01:

    alphaEN = st.number_input("Regression strength", min_value=0.1, max_value=10.0, value=1, step=.1, key=11)
    l1 = st.number_input("L1 norm weight", min_value=0.00, max_value=1.00, value=.50, step=.01, key=12)


    st.write("Elastic net")

    enm = ElasticNet(alpha=alphaEN, l1_ratio=l1)
    enm = enm.fit(X,y)
    enInt = round(enm.intercept_,2)
    enCoef = enm.coef_,2

    st.write("$hat{y} = %0.2f + %0.2fx_1 + %.02fx_2 + %.02fx_3 + %.02fx_4 + %.02fx_5 + %.02fx_6" %(enInt, round(enCoef[0],2), round(enCoef[1],2), round(enCoef[2],2), round(enCoef[3],2), round(enCoef[4],2), round(enCoef[5],2) ))

    enBias = (1/len(y))*((y-enm.predict(X)).sum())
    st.write("Bias = ", enBias)

    enEVar = (y-enm.predict(X)).var()

    st.write("Error variance = ", round(enEar, 4))

with col02: 
    fig, ax = plt.subplots()
    p = sns.scatterplot(x = enm.predict(X), y = y)
    p.set_xlabel('Predicted y', fontsize=14)
    p.set_ylabel('Actual y', fontsize=14)
    st.pyplot(fig)

    plot_description = st.checkbox("Show plot description?")

    if plot_description:
        st.write("Scatter plot with predicted y on the horizontal axis and actual y on the vertical axis.")
