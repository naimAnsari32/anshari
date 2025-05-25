import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

st.title("Linear Regression - Value for real home")

# CSV से वास्तविक डेटा लोड करना (उदाहरण के लिए)
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')
X = df[['rm']].values    # 'rm' = औसत कमरों की संख्या
y = df['medv'].values    # 'medv' = मध्य कीमत (हजार डॉलर में)

# मॉडल ट्रेन करना
model = LinearRegression()
model.fit(X, y)

# Streamlit स्लाइडर से इनपुट
user_rm = st.slider("your house rooms:", float(X.min()), float(X.max()), float(X.mean()))
pred_price = model.predict([[user_rm]])[0]

st.write(f"predicted room value ({user_rm} rooms):", round(pred_price, 2), "thousand dollar")

# Visualization
plt.scatter(X, y, color='gray', alpha=0.3, label='Real Data')
plt.plot(X, model.predict(X), color='red', label='Linear Fit')
plt.xlabel("Average rooms quantity")
plt.ylabel("Average value ($1000s)")
plt.legend()
st.pyplot(plt)