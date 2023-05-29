import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header

import mysql.connector as connection

db= connection.connect( host= "relational.fit.cvut.cz", database="PremierLeague",user="guest",passwd="relational",use_pure=True)

colored_header(label="Premier League's Season Dashboard",
               description= "this website is created using streamlit to show statistic of Players and Teams for this particular season as available in the dataset gotten from CTU Prague Relational Learning Repository\nrelational.fit.cvut.cz",
              color_name="green-90")


img=Image.open("fpl 4.jpeg")
st.sidebar.image(img.resize((1280,780)))

st.image("fpl 3.jpeg",use_column_width= True)

tm=pd.read_sql_query("select * from Teams",db)
pl=pd.read_sql_query("select * from Players",db)
ac=pd.read_sql_query("select * from Actions",db)
mt=pd.read_sql_query("select * from Matches",db)


### merging dataframes
data1=pd.merge(ac,tm,)
data2=pd.merge(ac,pl)



st.sidebar.title("TEAMS")
t_m= st.sidebar.selectbox("",data1["Name"].unique())
filter_data1= data1[(data1["Name"]==t_m)]

st.sidebar.title("PLAYERS")
p_l=st.sidebar.selectbox("",data2["Name"].unique())
filter_data2=data2[(data2["Name"]==p_l)]

st.title("Teams Season Stat")
st.write(filter_data1)

st.title("Players Season Stat")
st.write(filter_data2)


## creating the figsize and objects
st.title("Team Visualization Board")
fig1,(ax1,ax2)=plt.subplots(ncols=2,figsize=(10,5),facecolor="yellow")

## Create a BARCHART

ax1.bar(filter_data1["Name"],filter_data1["Goals"].sum())
ax1.set_xlabel("Team")
ax1.set_ylabel("Goals Scored")
ax1.set_title("Teams Vs Goal Scored")

ax2.bar(filter_data1["Name"],filter_data1["GoalsConceded"].sum())
ax2.set_xlabel("Team")
ax2.set_ylabel("Goals Conceded")
ax2.set_title("Teams Vs Goal Conceded")


st.pyplot(fig1)

st.title("Player Visualization Board")
fig2,(bx1,bx2)=plt.subplots(ncols=2,figsize=(10,5),facecolor="grey")

## Create a BARCHART

bx1.bar(filter_data2["Name"],filter_data2["Goals"].sum())
bx1.set_xlabel("Player")
bx1.set_ylabel("Goals Scored")
bx1.set(yticks=range(0,15))
bx1.set_title("Total Goal Scored")

bx2.bar(filter_data2["Name"],filter_data2["Assists"].sum())
bx2.set_xlabel("Player")
bx2.set_ylabel("Numbers Assit")
bx2.set(yticks=range(0,15))
bx2.set_title("Total Assist")

st.pyplot(fig2)






