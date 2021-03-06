import streamlit as st
import pandas as pd
df = pd.read_csv('Big_Brother_Edited.csv')
st.sidebar.markdown('''Here, you have the option to select the earliest year of players to consider''')
first_year = st.sidebar.slider("Select the First Year", 2000, 2020)
st.sidebar.markdown('''Here, you can to select the final year which will be considered''')
last_year = st.sidebar.slider("Select the Last Year", first_year, 2020)
race = st.sidebar.selectbox("Here you may select the race of the players you would like to look at", ['armenian', 'asian', 'black', 'black/asian', 'hispanic', 'latinx', 'middle eastern', 'pacific islander', 'portuguese', 'unknown', 'white'])
gender = st.sidebar.selectbox("Here you may select the gender of the players you would like to look at", ['male', 'female'])
vetos = st.sidebar.slider('Select the minimum number of vetos these players have won', 0, 5)
hoh = st.sidebar.slider('Select the minimum number of head of households these players have won', 0, 5)
st.title(f'Big Brother Players Between {first_year} and {last_year}')
just_these_years = (df.year >= first_year) & (df.year <= last_year)
just_this_race = df.oringal_race_ethnicity == race
just_this_gender = df.gender == gender
this_many_vetos = df.total_vetos >= vetos
this_many_hoh = df.total_hoh >= hoh
focus = df[just_these_years & just_this_race & just_this_gender & this_many_vetos & this_many_hoh]

st.write(f'These are the Big Brother Houseguests which fulfill your requests')
if len(focus) >0:
  st.write(focus[['name', 'final_placement','brand', 'brand_season', 'year', 'age', 'final_eviction_day', 'total_vetos', 'total_hoh', 'total_nominations', 'oringal_race_ethnicity']].reset_index( drop=True ))
else:
  st.write("No houseuest fulfill those requirements, adjust and try again.")
import matplotlib.pyplot as plt
plt.hist(focus['final_placement'], bins = 17, rwidth = .8)
plt.gcf().set_size_inches(8,10)
plt.title( f'Final Place of Selected \n Houseguests between \n{first_year} and {last_year}', fontsize=20 )
plt.xticks( range(0,18) )
plt.ylabel( 'Frequency', fontsize=14 )
plt.xlabel( 'Place' )
st.pyplot(plt.gcf())
st.write("To see all of my code, datasets, and the associated report, follow this link: https://github.com/lmgriffin13/Big-Brother")
st.write("To see my deepnote code which is discussed in my report, follow this link: https://deepnote.com/project/3091718b-48ae-4e42-a604-c0d8f6545ab4")
st.write("To see my final report, follow this link: https://github.com/lmgriffin13/Big-Brother/blob/main/MA%20346%20Final%20Report.docx")
st.write("Thank you to Vince Dixon whose work with the dataset can be seen here: https://vincedixonportfolio.com/app/big-brother-diversity/")
