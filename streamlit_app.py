import streamlit as st
import modelbit

def get_weather_info(location_id):
    try:
        result = modelbit.get_inference(
            region="ap-south-1",
            workspace="mustafaansari",
            deployment="get_weather_info",
            data=str(location_id)
        )
        return result['data']
    except Exception as e:
        return str(e)

def main():
    st.title("Weather Information App")
    location = st.text_input("Enter city or zip code:")
    if st.button("Get Weather"):
        weather_info = get_weather_info(location)
        for line in weather_info.split('\n'):
            st.write(line)

    # Sidebar
    st.sidebar.title("Weather Information App")
    st.sidebar.subheader("Developer Contact")
    st.sidebar.write("Name: Mustafa Ansari")
    st.sidebar.write("linkedin:https://www.linkedin.com/in/mustafaansaari/")

    st.sidebar.subheader("About")
    st.sidebar.write("This is a simple Streamlit app that provides weather information based on the input city or zip code.")
    st.sidebar.write("It uses a machine learning model deployed on modelbit for weather predictions.")

if __name__ == "__main__":
    main()
