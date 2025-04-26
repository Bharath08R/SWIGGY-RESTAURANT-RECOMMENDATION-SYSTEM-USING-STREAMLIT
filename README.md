📜 Project Overview
This project is a machine learning-based recommendation system that helps users discover restaurants based on their preferences such as city, cuisine, restaurant name, rating, and cost.
It utilizes a combination of data preprocessing, One-Hot Encoding, cosine similarity, and a Streamlit app for easy interaction.

🧠 Problem Statement
In today's fast-paced world, users demand personalized experiences.
Our goal is to recommend restaurants based on individual user preferences like city, cuisine type, and budget.

🔥 Business Use Cases
Personalized Recommendations: Helping users discover restaurants suited to their taste.

Improved Customer Experience: Making decision-making easier and faster.

Market Insights: Understanding popular user preferences across cities.

Operational Efficiency: Helping businesses align offerings to customer demands.

🛠️ Approach
Data Understanding and Cleaning

Remove duplicates and handle missing values.

Clean cost, rating, and rating_count columns.

Save the cleaned dataset (cleaned_data.csv).

Data Preprocessing

Apply One-Hot Encoding to categorical columns: name, city, and cuisine.

Save the encoded dataset (encoded_data.csv) and the encoder (encoder.pkl).

Recommendation Methodology

Use cosine similarity to recommend similar restaurants based on user preferences.

Map results back to the original (human-readable) cleaned data.

Streamlit Application

User inputs preferences through sidebar selection.

Outputs top recommended restaurants dynamically.

📂 Project Structure
bash
Copy
Edit
restaurant-recommendation/
│
├── cleaned_data.csv            # Cleaned restaurant dataset
├── encoded_data.csv             # One-hot encoded dataset
├── encoder.pkl                  # Saved OneHotEncoder object
├── app.py                       # Streamlit application
├── README.md                    # Project documentation
└── requirements.txt             # Project dependencies (optional)
🚀 How to Run Locally
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/restaurant-recommendation.git
cd restaurant-recommendation
Install Dependencies

bash
Copy
Edit
pip install pandas scikit-learn streamlit
(You can also include a requirements.txt file.)

Run the Streamlit App

bash
Copy
Edit
streamlit run app.py
Open your browser and navigate to:
http://localhost:8501

🎯 Results
Interactive Streamlit app for personalized restaurant recommendations.

Cleaned datasets for further analysis.

Cosine similarity-based recommendation engine.

Fully beginner-friendly and expandable project.

📊 Sample Screenshot
(You can add a screenshot of your Streamlit app here after running it.)

✨ Future Enhancements
Include external data (e.g., weather, holidays) to enhance recommendations.

Add user ratings and feedback to fine-tune suggestions.

Implement deep learning models for better personalization.

🤝 Acknowledgments
Dataset: Collected from Swiggy restaurant data sources.

Libraries: Pandas, Scikit-learn, Streamlit.
