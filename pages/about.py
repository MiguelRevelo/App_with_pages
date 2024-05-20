import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("About this app", className="about-title"),
        html.P(
            "This app is a fitness and health tracker that helps you keep track of your daily activities and health metrics."
        ),
        html.P(
            "You can use this app to track your daily steps, calories burned, sleep hours, and more."
        ),
        html.P(
            "The app also provides you with recommendations on how to improve your health and fitness."
        ),
        html.P(
            "The app also provides you with statistics on your fitness and health metrics to help you track your progress."
        ),
        html.P(
            "The app also provides you with exercises to help you stay fit and healthy."
        ),
        html.P(
            "The app also provides you with AI assistance to help you with your fitness and health goals."
        ),
    ]
)
