import numpy as np
import dill
import streamlit as st

# Load the model
loaded_model = dill.load(open('E:/Code/myProjects/recommendation-system/movies_recommender.sav', 'rb'))

# Create a function to récommend the movie
def recommend_movies(movie_name):
    return loaded_model.recommend(movie_name)

for i in recommend_movies('Iron Man'):
    print(i)

def main():
    st.title('Movie Recommender System')
    movie_name = st.text_input('Enter the name of the movie')
    
    if st.button('Recommend'):
        recommended_movies = recommend_movies(movie_name)
        for i in recommended_movies:
            st.write(i)

if __name__ == '__main__':
    main()