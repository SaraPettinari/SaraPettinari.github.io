import plotly.express as px
import os
import pandas as pd

# List of visited places with coordinates
visited_places = [
    {"city": "Aachen", "lat": 50.7753, "lon": 6.0839, "description": "Process Mining Summer School (2022)"},
    {"city": "Corfù", "lat": 39.6200, "lon": 19.9111, "description": "Summer School on Robotics and STEM in Schools (2022)"},
    {"city": "Bremen", "lat": 53.0793, "lon": 8.8017, "description": "Robotics Software Engineering Meeting (RSE 2024)"},
    {"city": "Rome", "lat": 41.9028, "lon": 12.4964, "description": "International Conference on Process Mining (ICPM 2023)"},
    {"city": "Copenhagen", "lat": 55.6761, "lon": 12.5683, "description": "International Conference on Process Mining (ICPM 2024)"},
    {"city": "Falerna Marina", "lat": 38.9978324, "lon": 16.1320568, "description": "International Conference on Pervasive Intelligence and Computing (PICom 2022)"},
    {"city": "Bari", "lat": 41.1171, "lon": 16.8719, "description": "Convegno Italiano sulla Didattica dell’Informatica (ITADINFO 2024)"},
    {"city": "Lucca", "lat": 43.8410, "lon": 10.5042, "description": "International Conference on Coordination Models and Languages (COORDINATION 2022)"},
    {"city": "Eindhoven", "lat": 51.4415, "lon": 5.4697, "description": "3 months visiting @ TU/e (2023)"},
    {"city": "Groningen", "lat": 53.2194, "lon": 6.5665, "description": "International Conference on Enterprise Design, Operations and Computing (EDOC 2023)"},
    {"city": "Vienna", "lat": 48.210033, "lon": 16.363449, "description": "International Conference on Advanced Information Systems Engineering (CAiSE 2025)"},
    {"city": "Gent", "lat": 51.049999, "lon": 3.733333, "description": "Internet of Processes and Things Meeting (2025)"},
    {"city": "Odense", "lat": 55.3997225, "lon": 10.3852104, "description": "Robotics Software Engineering Meeting (RSE 2025)"},
    {"city": "Montevideo", "lat": -34.9011, "lon": -56.1645, "description": "International Conference on Process Mining (ICPM 2025)"},
]

# Convert to DataFrame
df = pd.DataFrame(visited_places)

# Generate the map with enhanced visuals
fig = px.scatter_map(
    df,
    lat="lat",
    lon="lon",
    hover_name=None,  # Suppress hover name (city name)
    hover_data={"city": True, "description": True},  # Show only the description
    #projection="natural earth",
    color='city',  # Optional: Use city for color coding
    size_max=15,  # Maximum size of the markers
    size=[10] * len(df),  # Set a default size for all markers
    zoom=1,
)

# Update hovertemplate to show only description
fig.update_traces(hovertemplate='<b> 📍 %{customdata[0]}:</b> %{customdata[1]}<extra></extra> ')


# Customize layout for a more visually appealing look
fig.update_layout(
    geo=dict(
        showland=True,
        landcolor='whitesmoke',  # Land color
        subunitcolor='lightgrey',  # Subunit borders
        countrycolor='darkgrey',  # Country borders
        coastlinecolor='darkgrey',  # Coastline color
    ),
    margin=dict(l=0, r=0, t=40, b=0),  # Adjust margins
    font=dict(size=14, family='Arial', color='black'),  # Font for text and hover
    paper_bgcolor='rgba(255, 255, 255, 1)',  # Background color for the map
    showlegend=False,
)

# Save map as an HTML file
fig.write_html(os.getcwd() + "/assets/maps/visited_places_map.html")

# Optionally, save as an image (requires orca installation)
# fig.write_image("/path_to_save/visited_places_map.png")
