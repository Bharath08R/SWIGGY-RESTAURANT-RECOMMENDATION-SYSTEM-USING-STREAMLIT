import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load data and encoder
cleaned_df = pd.read_csv("cleaned_data.csv")
encoded_df = pd.read_csv("encoded_data.csv")

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Recommendation function
def recommend_restaurants(user_input, encoder, encoded_df, cleaned_df, top_n=5):
    user_df = pd.DataFrame([user_input])
    user_encoded = encoder.transform(user_df)
    user_encoded_df = pd.DataFrame(user_encoded, columns=encoder.get_feature_names_out())
    
    for col in encoded_df.columns:
        if col not in user_encoded_df.columns:
            user_encoded_df[col] = 0
            
    user_encoded_df = user_encoded_df[encoded_df.columns]
    
    similarities = cosine_similarity(user_encoded_df, encoded_df)
    top_indices = similarities[0].argsort()[-top_n:][::-1]
    recommendations = cleaned_df.iloc[top_indices]
    return recommendations

# Streamlit UI
st.title("🍽️ Restaurant Recommendation System")
st.write("Get personalized restaurant recommendations based on your preferences!")

# Sidebar Inputs
st.sidebar.header("User Preferences")

name = st.sidebar.selectbox("Select Restaurant Name (or similar)", cleaned_df['name'].unique())
city = st.sidebar.selectbox("Select City", cleaned_df['city'].unique())
cuisine = st.sidebar.selectbox("Select Cuisine", cleaned_df['cuisine'].unique())

top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# Get recommendations on button click
if st.sidebar.button("Get Recommendations"):
    user_input = {
        'name': name,
        'city': city,
        'cuisine': cuisine
    }
    
    recommendations = recommend_restaurants(user_input, encoder, encoded_df, cleaned_df, top_n)
    
    st.subheader("Top Recommended Restaurants for You:")
    for index, row in recommendations.iterrows():
        st.markdown(f"**🍴 {row['name']}**")
        st.write(f"City: {row['city']}")
        st.write(f"Cuisine: {row['cuisine']}")
        st.write(f"⭐ Rating: {row['rating']}")
        st.write(f"💵 Cost for Two: ₹{int(row['cost'])}")
        st.write("---")

