import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
#add title
st.title('Data Analysis Applications')
st.subheader('This is a simple data analysis application created by Naim Ansari')

#creat a dropdown list to choose a dataset
dataset_options=['iris','titanic','tips','diamonds']
selected_dataset=st.selectbox('Select a dataset',dataset_options)

#load the selected dataset
if selected_dataset == 'iris':
   df=sns.load_dataset('iris')
elif selected_dataset == 'titanic':
   df=sns.load_dataset('titanic')
elif selected_dataset == 'tips':
   df=sns.load_dataset('tips')
elif selected_dataset =='diamonds':
   df=sns.load_dataset('diamonds')

#button to upload custom dataset
uploaded_file=st.file_uploader('upload a custom dataset',type=['csv','xlsx'])
# If a file is uploaded, read it into a DataFrame
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("Custom dataset loaded successfully!")
    except Exception as e:
        st.error(f"Error loading file: {e}")

# Dataset Preview Section
st.markdown("## Dataset Preview")
# Expander to show the first few rows of the DataFrame
with st.expander("Show DataFrame Head"):
    st.dataframe(df.head())

# Display basic dataset metrics: number of rows, columns, and total missing values
col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())

# Data Types & Missing Values
# Expander to show data types, missing values, and unique value counts for each column
with st.expander("Show Data Types & Missing Values"):
    st.write(pd.DataFrame({
        "Data Type": df.dtypes,
        "Missing Values": df.isnull().sum(),
        "Unique Values": df.nunique()
    }))

# Descriptive Statistics
st.markdown("## Descriptive Statistics")

# Expander for numerical features summary (mean, std, min, max, etc.)
with st.expander("Numerical Features Summary"):
    st.write(df.describe())

# Expander for categorical features summary (value counts)
with st.expander("Categorical Features Summary"):
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(cat_cols) > 0:
        for col in cat_cols:
            st.write(f"**{col}**")
            st.write(df[col].value_counts())
    else:
        st.info("No categorical columns found.")

# Correlation Heatmap
st.markdown("## Correlation Heatmap")
# Select only numerical columns for correlation analysis
num_cols = df.select_dtypes(include=np.number).columns
if len(num_cols) > 1:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
else:
    st.info("Not enough numerical columns for correlation heatmap.")

# Interactive Visualizations
st.markdown("## Interactive Visualizations")
# Dropdown to select the type of plot
plot_type = st.selectbox("Choose plot type", ["Histogram", "Boxplot", "Scatterplot", "Pairplot"])

# Histogram plot for a selected numerical column
if plot_type == "Histogram":
    col = st.selectbox("Select column for histogram", num_cols)
    bins = st.slider("Number of bins", 5, 100, 30)
    fig, ax = plt.subplots()
    sns.histplot(df[col].dropna(), bins=bins, kde=True, ax=ax, color='skyblue')
    ax.set_title(f"Histogram of {col}")
    st.pyplot(fig)
# Boxplot for a selected numerical column, optionally grouped by a categorical column
elif plot_type == "Boxplot":
    col = st.selectbox("Select column for boxplot", num_cols)
    group_col = st.selectbox("Group by (optional)", [None] + list(cat_cols))
    fig, ax = plt.subplots()
    if group_col and group_col in df.columns:
        sns.boxplot(x=df[group_col], y=df[col], ax=ax, palette='Set2')
    else:
        sns.boxplot(y=df[col], ax=ax, color='lightgreen')
    ax.set_title(f"Boxplot of {col}")
    st.pyplot(fig)

# Scatterplot for two selected numerical columns, optionally colored by a categorical column
elif plot_type == "Scatterplot":
    col_x = st.selectbox("X-axis", num_cols, key="scatter_x")
    col_y = st.selectbox("Y-axis", num_cols, key="scatter_y")
    hue = st.selectbox("Color by (optional)", [None] + list(cat_cols))
    fig, ax = plt.subplots()
    if hue and hue in df.columns:
        sns.scatterplot(x=df[col_x], y=df[col_y], hue=df[hue], ax=ax, palette='tab10')
    else:
        sns.scatterplot(x=df[col_x], y=df[col_y], ax=ax, color='coral')
    ax.set_title(f"Scatterplot: {col_x} vs {col_y}")
    st.pyplot(fig)
# Pairplot for all numerical columns (may be slow for large datasets)
elif plot_type == "Pairplot":
    st.info("Generating pairplot (may take a while for large datasets)...")
    fig = sns.pairplot(df[num_cols].dropna(), diag_kind='kde')
    st.pyplot(fig)
# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Made with ❤️ by Naim Ansari | Powered by Streamlit, Seaborn, Pandas"
    "</div>",
    unsafe_allow_html=True
)