import streamlit as st
import random
import time
import csv

# Streamlit App Title with emojis and colorful, smaller font
st.markdown("""
    <h1 style='color: #FF6347; font-size: 25px; text-align: center;'>🎬 Welcome Movie Superstar! 🌟 All the best..!!</h1>
""", unsafe_allow_html=True)

# Load the movie list from the CSV file
def load_movies_from_csv(csv_file):
    try:
        # Open and read the CSV file using Python's built-in csv module
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            movie_list = [row[0] for row in reader if row]  # Assuming the movie name is in the first column
            
        # Remove any leading/trailing whitespaces from the movie names
        movie_list = [movie.strip() for movie in movie_list if movie.strip()]
        
        # Check if the movie list is empty
        if not movie_list:
            st.error("No movies found in the CSV file.")
            return []
        
        return movie_list
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        return []

# Streamlit App Title for the "Spin The Wheel" with reduced font size
st.markdown("<h2 style='font-size: 20px; text-align: center;'>Spin The Wheel 🎉</h2>", unsafe_allow_html=True)
st.write("Click the button to spin the wheel and get a random Hindi movie 🎥🍿.")

# Load movies from the CSV file
movie_list = load_movies_from_csv("movies.csv")  # Adjust the path as necessary

# Check if the movie list is loaded properly
if not movie_list:
    st.error("Failed to load the movie list from the CSV.")
else:
    # Add a button to start the spin
    if st.button("Spin This Wheel 🎰"):
        # Show a spinning animation (for 3 seconds)
        with st.spinner("Spinning the wheel... please wait! ⏳"):
            time.sleep(3)  # Simulate the spinning time of 3 seconds
        
        # Randomly select a movie after the spin ends
        movie = random.choice(movie_list)
        
        # Display the movie with a smaller font size and blue color
        st.markdown(f"<h3 style='color: #0000FF; font-size: 24px; text-align: center;'>Movie Selected: {movie} 🎬🎉</h3>", unsafe_allow_html=True)
