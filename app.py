import streamlit as st
import pandas as pd
import matplotlib as plt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Student Performance Dashboard")

# Load data
df = pd.read_csv("data/StudentsPerformance.csv")

# Create average score column
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Show data
st.subheader("Dataset Preview")
st.write(df.head())

# Filter by gender
gender = st.selectbox("Select Gender", df['gender'].unique())
filtered_df = df[df['gender'] == gender]

# Show filtered data
st.subheader(f"Filtered Data ({gender})")
st.write(filtered_df)

# Plot histogram of average scores
st.subheader("Average Score Distribution")
fig, ax = plt.subplots()
ax.hist(filtered_df['average_score'], bins=10, color='skyblue', edgecolor='black')
ax.set_xlabel("Average Score")
ax.set_ylabel("Number of Students")
ax.set_title("Distribution of Average Scores")
st.pyplot(fig)

# Boxplot of Average Scores
st.subheader("Boxplot of Average Scores")
fig2, ax2 = plt.subplots()
ax2.boxplot(filtered_df['average_score'])
ax2.set_ylabel("Average Score")
ax2.set_title("Boxplot of Average Scores")
st.pyplot(fig2)


# Scatterplot: Math vs Reading
st.subheader("Math Score vs Reading Score")
fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df['math score'], filtered_df['reading score'], color='green', alpha=0.6)
ax3.set_xlabel("Math Score")
ax3.set_ylabel("Reading Score")
ax3.set_title("Math Score vs Reading Score")
st.pyplot(fig3)

fig.savefig("images/histogram.png")
fig2.savefig("images/boxplot.png")
fig3.savefig("images/math_vs_reading.png")