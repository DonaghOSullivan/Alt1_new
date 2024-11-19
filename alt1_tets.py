import subprocess

# Try a different port (e.g., 8502)
process = subprocess.Popen([
    "streamlit", "run", "StreamLit_Alt1.py",
    "--server.port", "851",
    "--server.headless", "true"
])

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'Alt1_exG_DataBase(in).csv'  # Ensure your CSV file is in the same directory as this script
data = pd.read_csv(file_path)

# Streamlit app
st.title("Football Statistics Visualizer")
st.write("Select a club and a stat to visualize the data.")

# Dropdown 1: Select Club
clubs = data['Team'].unique()
selected_club = st.selectbox("Select a Club", clubs)

# Dropdown 2: Select Stat
stats = {
    "Most Goals": "Actual Goals",
    "Most Expected Goals": "Expected Goals (xG)",
    "Biggest Goal Difference": "Goal difference"
}
selected_stat = st.selectbox("Select a Stat", list(stats.keys()))

# Filter data based on the selected club
filtered_data = data[data['Team'] == selected_club]

# Extract the relevant column for visualization
stat_column = stats[selected_stat]

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(filtered_data['Player'], filtered_data[stat_column], color='skyblue')
ax.set_title(f"{selected_stat} for {selected_club}", fontsize=16)
ax.set_xlabel("Player", fontsize=12)
ax.set_ylabel(stat_column, fontsize=12)
plt.xticks(rotation=45)

# Display the plot in Streamlit
st.pyplot(fig)