import streamlit as st
import random
import time
import pandas as pd

# Streamlit App Title with emojis and colorful, smaller font
st.markdown("""
    <h1 style='color: #FF6347; font-size: 25px; text-align: center;'>🎬 Welcome Movie Superstar! 🌟 All the best..!!</h1>
""", unsafe_allow_html=True)

# Load the movie list from the CSV file
def load_movies_from_csv(csv_file):
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(csv_file)
        
        # Ensure we only have the 'MovieName' column, and remove any rows with NaN values
        if 'MovieName' not in df.columns:
            st.error("CSV file must have a 'MovieName' column.")
            return []
        
        # Get the movie names as a list
        movie_list = df['MovieName'].dropna().tolist()
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
