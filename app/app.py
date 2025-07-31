import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title("🧠 Personality Type Predictor")

st.markdown("Fill in the following personality traits to get your prediction:")

# UI inputs
social_energy = st.slider("Social Energy", 1, 10, 5)
alone_time_preference = st.slider("Alone Time Preference", 1, 10, 5)
talkativeness = st.slider("Talkativeness", 1, 10, 5)
deep_reflection = st.slider("Deep Reflection", 1, 10, 5)
group_comfort = st.slider("Comfort in Groups", 1, 10, 5)
party_liking = st.slider("Party Liking", 1, 10, 5)
listening_skill = st.slider("Listening Skill", 1, 10, 5)
empathy = st.slider("Empathy", 1, 10, 5)
creativity = st.slider("Creativity", 1, 10, 5)
organization = st.slider("Organization", 1, 10, 5)
leadership = st.slider("Leadership", 1, 10, 5)
risk_taking = st.slider("Risk Taking", 1, 10, 5)
public_speaking_comfort = st.slider("Public Speaking Comfort", 1, 10, 5)
curiosity = st.slider("Curiosity", 1, 10, 5)
routine_preference = st.slider("Routine Preference", 1, 10, 5)
excitement_seeking = st.slider("Excitement Seeking", 1, 10, 5)
friendliness = st.slider("Friendliness", 1, 10, 5)
emotional_stability = st.slider("Emotional Stability", 1, 10, 5)
planning = st.slider("Planning", 1, 10, 5)
spontaneity = st.slider("Spontaneity", 1, 10, 5)
adventurousness = st.slider("Adventurousness", 1, 10, 5)
reading_habit = st.slider("Reading Habit", 1, 10, 5)
sports_interest = st.slider("Sports Interest", 1, 10, 5)
online_social_usage = st.slider("Online Social Usage", 1, 10, 5)
travel_desire = st.slider("Desire to Travel", 1, 10, 5)
gadget_usage = st.slider("Gadget Usage", 1, 10, 5)
work_style_collaborative = st.slider("Collaborative Work Style", 1, 10, 5)
decision_speed = st.slider("Decision Speed", 1, 10, 5)
stress_handling = st.slider("Stress Handling", 1, 10, 5)

if st.button("Predict Personality"):
    try:
        # Load saved files
        model = joblib.load(r'C:\Users\saeem\Desktop\Introvert\personality_classifier.pkl')
        scaler = joblib.load(r'C:\Users\saeem\Desktop\Introvert\scaler.pkl')
        encoder = joblib.load(r'C:\Users\saeem\Desktop\Introvert\label_encoder.pkl')
        feature_columns = joblib.load(r'C:\Users\saeem\Desktop\Introvert\feature_columns.pkl')

        # Collect input in correct order
        input_values = [
            social_energy, alone_time_preference, talkativeness, deep_reflection,
            group_comfort, party_liking, listening_skill, empathy, creativity, organization,
            leadership, risk_taking, public_speaking_comfort, curiosity, routine_preference,
            excitement_seeking, friendliness, emotional_stability, planning, spontaneity,
            adventurousness, reading_habit, sports_interest, online_social_usage, travel_desire,
            gadget_usage, work_style_collaborative, decision_speed, stress_handling
        ]

        # Construct input DataFrame with correct columns
        input_df = pd.DataFrame([input_values], columns=feature_columns)

        # Scale and predict
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        personality = encoder.inverse_transform(prediction)[0]

        st.markdown(
            f"<h2 style='text-align: center; color: #00C8FF;'>🎯 Predicted Personality:<b>{personality}</b></h2>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
