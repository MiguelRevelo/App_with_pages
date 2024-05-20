import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("Recommendations", className="recommendations-title"),
        html.H2("Ingesta de calorias diarias"),
        html.P(
            "Para calcular la tasa metabolica basal, se puede utilizar la formula de Harris-Benedict:"
        ),
        html.P(
            "Hombres: [88.362 + (13.397 x peso en kg) + (4.799 x altura en cm) - (5.677 x edad en años)]x factor de actividad"
        ),
        html.P(
            "Mujeres: [447.593 + (9.247 x peso en kg) + (3.098 x altura en cm) - (4.330 x edad en años)] x factor de actividad"
        ),
        html.P(
            "Donde el factor de actividad es 1.2 para sedentario, 1.375 para ligero, 1.55 para moderado, 1.725 para activo y 1.9 para muy activo"
        ),
        html.H2("Indice de masa corporal"),
        html.P(
            "El indice de masa corporal es una medida de la grasa corporal en base a la estatura y el peso y calculado como IMC = peso en kg / (altura en m)^2"
        ),
        html.H3("Criterios de evaluacion"),
        html.P("Bajo peso: IMC < 18.5"),
        html.P("Normal: 18.5 <= IMC < 24.9"),
        html.P("Sobrepeso: 25 <= IMC < 29.9"),
        html.P("Obesidad: IMC >= 30"),
        # Add box to calculate BMI and BMR
        html.H2("Informacion sobre el pulso"),
        html.P("El pulso es la cantidad de veces que late el corazon por minuto"),
        html.P("El pulso normal es de 60-100 latidos por minuto"),
        html.P(
            "Para adultos, el rango normal de pulso en reposo suele estar entre 60 y 100 latidos por minuto (bpm).  Pulsaciones menores o mayores pueden ser peligrosas Un rango objetivo común para la frecuencia cardíaca durante el ejercicio varía entre el 50% y el 85% de la frecuencia cardíaca máxima prevista de una persona. La fórmula básica para estimar la frecuencia cardíaca máxima es 220 menos la edad. (220-edad)*0.85 (Pulsaciones mayores a esta pueden ser peligrosas, si se está haciendo ejercicio)"
        ),
        html.P(
            "El pulso puede ser afectado por la edad, el sexo, la actividad fisica y la salud"
        ),
    ],
)
