import streamlit as st
import random
import time
import csv
import os

# Streamlit App Title with emojis and colorful, smaller font
st.markdown("""
    <h1 style='color: #FF6347; font-size: 25px; text-align: center;'>🎬 Welcome Movie Superstar! 🌟 All the best..!!</h1>
""", unsafe_allow_html=True)

# Function to load movie list from CSV
def load_movies_from_csv(csv_file):
    try:
        # Open the CSV file and read the movie names
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            movie_list = [row['MovieName'] for row in reader if row['MovieName']]
        return movie_list
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        return []

# Timer functionality
def start_timer(duration, time_remaining_placeholder):
    """Simulate a countdown timer for the given duration (in seconds)."""
    st.session_state.time_left = duration  # Initialize time in session state
    time_remaining_placeholder.text("Time Remaining: 00:00")  # Initialize with 00:00

    while st.session_state.time_left > 10:
        minutes, seconds = divmod(st.session_state.time_left, 60)
        st.session_state.time_left -= 1
        st.session_state.timer_running = True

        # Update the time left display in real-time
        st.session_state.time_display = f"{minutes:02d}:{seconds:02d}"
        time_remaining_placeholder.text(f"Time Remaining: {st.session_state.time_display}")  # Update the placeholder

        time.sleep(1)  # Decrease time every second

    # Flashing countdown for the last 10 seconds
    flashing_placeholder = st.empty()  # Placeholder for flashing numbers
    for i in range(10, 0, -1):
        flashing_placeholder.markdown(f"<h1 style='color: red; font-size: 70px; text-align: center;'>" + str(i) + "</h1>", unsafe_allow_html=True)
        time.sleep(0.8)  # Flash every 0.8 second

    # Finally show '0' in large size
    flashing_placeholder.markdown(f"<h1 style='color: red; font-size: 70px; text-align: center;'>0</h1>", unsafe_allow_html=True)

    # When timer ends, announce "Time's up!"
    st.session_state.timer_running = False
    st.session_state.time_display = "00:00"
    
    # Play a random audio file when the time is up
    audio_folder = "audio"  # Path to the audio folder
    
    # Ensure the audio folder exists and contains audio files
    if os.path.exists(audio_folder) and os.listdir(audio_folder):
        # Get all audio files from the folder
        audio_files = [f for f in os.listdir(audio_folder) if f.endswith(('.mp3', '.wav', '.ogg'))]
        
        # Select a random audio file
        random_audio = random.choice(audio_files)
        audio_path = os.path.join(audio_folder, random_audio)
        
        # Play the random audio file automatically
        st.audio(audio_path, format="audio/wav", autoplay=True)  # You can adjust the format depending on your file type
    else:
        st.warning("No audio files found in the 'audio' folder.")
    
    st.success("⏰ Time's up! 🎉")
    time_remaining_placeholder.text("Time Remaining: 00:00")  # Reset the placeholder text

    # Show balloon animation after a short delay
    time.sleep(2)  # Adjust this as necessary to allow audio to play for a bit
    st.snow()

# Initialize session state variables if they don't exist
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.time_left = 0
    st.session_state.time_display = "00:00"

# Load movies from the CSV file (assumes the CSV has a 'MovieName' column)
movie_list = load_movies_from_csv("movies.csv")  # Adjust the path as necessary

# Tabs using st.tabs
tabs = st.tabs(["Spin the Wheel", "Time Tracker"])

with tabs[0]:
    # Spin the Wheel Section
    st.markdown("<h2 style='font-size: 20px; text-align: center;'>Spin The Wheel 🎉</h2>", unsafe_allow_html=True)
    st.write("Click the button to spin the wheel and get a random Hindi movie 🎥🍿.")
    
    # Display the Spin Button
    if st.button("Spin This Wheel 🎰"):
        # Show a spinning animation (for 3 seconds)
        with st.spinner("Spinning the wheel... please wait! ⏳"):
            time.sleep(2)  # Simulate the spinning time of 3 seconds
        
        # Randomly select a movie after the spin ends
        if movie_list:
            movie = random.choice(movie_list)
            # Display the movie with a smaller font size and blue color
            st.markdown(f"<h3 style='color: #0000FF; font-size: 24px; text-align: center;'>Movie Selected: {movie} 🎬🎉</h3>", unsafe_allow_html=True)
        else:
            st.error("No movies available to select. Please check the CSV file.")

with tabs[1]:
    # Time Tracker Section
    st.markdown("<h2 style='font-size: 20px; text-align: center;'>Time Tracker 🕒</h2>", unsafe_allow_html=True)
    
    # Set Time Section
    st.write("### Set Timer (in minutes):")
    time_input = st.text_input("Enter time in minutes:", value="5")  # Default to 1 minute
    
    # Validate time input
    try:
        time_in_minutes = int(time_input)
        time_in_seconds = time_in_minutes * 60
    except ValueError:
        st.error("Please enter a valid integer for minutes.")
        time_in_seconds = 0
    
    # Create a placeholder for the time remaining display
    time_remaining_placeholder = st.empty()
    
    # Custom style for larger font size of "Time Remaining"
    st.markdown("""
    <style>
        .time-remaining {
            font-size: 40px;
            color: #FF6347;
            font-weight: bold;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Display Time Remaining with a custom class
    time_remaining_placeholder.markdown('<div class="time-remaining">Time Remaining: 00:00</div>', unsafe_allow_html=True)
    
    if time_in_seconds > 0 and not st.session_state.timer_running:
        if st.button("Start Timer"):
            start_timer(time_in_seconds, time_remaining_placeholder)  # Start the timer

    # Display the remaining time in the second column
    if st.session_state.timer_running:
        time_remaining_placeholder.markdown(f'<div class="time-remaining">Time Remaining: {st.session_state.time_display}</div>', unsafe_allow_html=True)
