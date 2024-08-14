import pickle
import pandas as pd
import streamlit as st

# load the data
data = pickle.load(open('movie_dict.pkl', mode = 'rb'))
data = pd.DataFrame(data)
#print(movies)

# load similarity score
similarity = pickle.load(open('Similarity.pkl', mode = 'rb'))
print(similarity)

# final function
# to print names of movies
def recommend(movie):
    recommended_movies = []
    movie_index = data[data['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x: x[1])[1:6]
    
    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)

    return recommended_movies

#print(data['title'].values)

# streamlit app library => we make web apps through this
st.title("Movie Recommendation System")

# command+j to open terminal

# streamlit code from streamlit documentation (search google)

selected_movie = st.selectbox(
    "Select a movie to get recommendations:",
    data['title'].values)

st.write("You selected:", selected_movie)

btn = st.button("Recommend")

if btn:
    list_of_movies = recommend(selected_movie)

    for movie in list_of_movies:
        #print(movie)  this output comes on terminal, but we want it on the website itself
        st.write(movie)

    # learn streamlit