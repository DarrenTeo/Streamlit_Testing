import plotly.express as px
import streamlit as st
import pandas as pd

df = px.data.gapminder()

st.subheader('Analysis')

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

st.plotly_chart(fig)

with st.sidebar:
    st.subheader('Dataset')
    df

    #####################
    ### Download Data ###
    #####################
    download_df = pd.DataFrame(df).to_csv(index=False,encoding='utf-8')
    st.download_button(
        label="Download CSV",
        data=download_df,
        file_name='Dataset.csv',
        mime='text/csv',)