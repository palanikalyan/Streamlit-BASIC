import streamlit as st
import requests
import datetime
import time  # Import the time module for adding delays

# Function to fetch COVID-19 data from the API
def get_covid_data():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()

    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    affected_countries = str(json_data['affectedCountries'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at / 1e3)

    return {
        "total_cases": total_cases,
        "total_deaths": total_deaths,
        "today_cases": today_cases,
        "today_deaths": today_deaths,
        "today_recovered": today_recovered,
        "affected_countries": affected_countries,
        "last_updated": date
    }

# Streamlit App
def main():
    # Splash screen simulation using time.sleep
    with st.spinner("Loading..."):
        st.title("Welcome to the COVID-19 Dashboard!")
        st.markdown("Stay home! Stay safe!")
        st.markdown("The app will load in a few seconds.")
        time.sleep(3)  # Simulates splash screen duration
        st.balloons()
    
    # App title
    st.title("Corona Virus Analysis")
    
    # Fetch COVID-19 data
    covid_data = get_covid_data()

    # Displaying data in the app
    st.header("Global COVID-19 Statistics")

    # Total Cases
    st.metric(label="Total Cases", value=covid_data['total_cases'])
    st.metric(label="Total Deaths", value=covid_data['total_deaths'])
    st.metric(label="Today Cases", value=covid_data['today_cases'])
    st.metric(label="Today Deaths", value=covid_data['today_deaths'])
    st.metric(label="Today Recovered", value=covid_data['today_recovered'])

    # Display affected countries
    st.subheader("Affected Countries")
    st.write(covid_data['affected_countries'])

    # Display last updated time
    st.subheader("Last Updated:")
    st.write(covid_data['last_updated'])

    # Load data button
    if st.button("Load COVID-19 Data"):
        covid_data = get_covid_data()
        st.write("Updated Data:")
        st.write(covid_data)

if __name__ == "__main__":
    main()
