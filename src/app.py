import gradio as gr
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

iface = gr.Interface(
    fn=get_weather_info,
    inputs=gr.Textbox(label="city name or zip code"),
    outputs=gr.Textbox(label="Weather Information"),
    title="Weather Information App",
    description="Enter a city name or zip code to get the weather information."
)

iface.launch()
