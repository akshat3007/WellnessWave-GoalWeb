import streamlit as st

def calculate_calories_burned(exercise_type, duration, weight):
    MET_values = {
        "cycling": 8.0,
        "walking": 3.5,
        "swimming": 8.0
    }
    MET = MET_values.get(exercise_type.lower(), 0)
    calories_burned = MET * 3.5 * weight * duration / 60
    return calories_burned

def calculate_daily_calorie_need(weight, height, age, gender):
    if gender.lower() == "male":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender.lower() == "female":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        return None
    return BMR * 1.55

# Streamlit App
st.title("Calorie Burn and Weight Management Calculator")

st.header("Input Your Details")
exercise_type = st.selectbox("Select exercise type:", ["cycling", "walking", "swimming"])
duration = st.number_input("Duration of exercise (minutes):", min_value=0, step=1)
weight = st.number_input("Weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Height (cm):", min_value=0.0, step=0.1)
calorie_intake = st.number_input("Daily calorie intake (kcal):", min_value=0.0, step=0.1)
age = st.number_input("Age (years):", min_value=0, step=1)
gender = st.selectbox("Gender:", ["male", "female"])

if st.button("Calculate"):
    calories_burned = calculate_calories_burned(exercise_type, duration, weight)
    daily_calorie_need = calculate_daily_calorie_need(weight, height, age, gender)

    if daily_calorie_need is None:
        st.error("Invalid gender input. Please select male or female.")
    else:
        net_calorie_deficit = daily_calorie_need - calorie_intake - calories_burned
        st.write(f"Calories burned during exercise: {calories_burned:.2f} kcal")
        st.write(f"Your daily calorie need: {daily_calorie_need:.2f} kcal")

        if net_calorie_deficit < 0:
            st.success("You are likely to lose weight.")
            weight_loss_per_week = net_calorie_deficit * 7 / 7700
            st.write(f"Estimated weight loss per week: {weight_loss_per_week:.2f} kg")
        else:
            st.info("You are not likely to lose weight.")
