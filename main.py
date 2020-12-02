import streamlit as st
import pandas as pd
df = pd.read_csv('Big_Brother_Edited.csv')
st.sidebar.markdown('''Here, you have the option to select the earliest year of players to consider''')
first_year = st.sidebar.slider("Select the First Year", 2000, 2020)
st.sidebar.markdown('''Here, you can to select the final year which will be considered''')
last_year = st.sidebar.slider("Select the Last Year", first_year, 2020)
st.sidebar.markdown('''Here, you have the option to select the race of the players you will look at which will be considered in your baseball data''')
race = st.sidebar.selectbox("Here you may select the race of the players you would like to look at", ['<select>','armenian', 'asian', 'black', 'black/asian', 'hispanic', 'latinx', 'middle eastern', 'pacific islander', 'portuguese', 'unknown', 'white'])
st.sidebar.markdown('''Here, you may select the gender of players to consider''')
gender = st.sidebar.selectbox("Here you may select the gender of the players you would like to look at", ['male', 'female'])
vetos = st.sidebar.slider('Select the number of vetos these players have won', 0, 5)
hoh = st.sidebar.slider('Select the number of head of households these players have won', 0, 5)
st.title(f'Big Brother Players Between {first_year} and {last_year}')
just_these_years = (df.year >= first_year) & (df.year <= last_year)
just_this_race = df.oringal_race_ethnicity == race
just_this_gender = df.gender == gender
this_many_vetos = df.total_vetos <= vetos
this_many_hoh = df.total_hoh <= hoh
focus = df[just_these_years & just_this_race & just_this_gender & this_many_vetos & this_many_hoh]

# Which years do we care about?
years = range( first_year, last_year )

st.write(f'These are the Big Brother Houseguests which fulfill your requests')
st.write(focus.reset_index( drop=True ))
st.write(len(focus))

