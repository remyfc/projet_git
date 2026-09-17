from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Correction : on définit proprement la plage d'années de 1996 à 2025 (inclus)
data = {
    "Année": list(range(1996, 2026)),
    "Indice_Prix": [
        68.5, 69.2, 70.1, 71.0, 72.8, 74.5, 76.2, 78.0, 79.5, 81.2, 
        83.0, 85.1, 86.2, 86.8, 88.5, 90.4, 92.2, 93.1, 93.3, 93.5, 
        94.2, 95.5, 97.0, 98.2, 99.0, 100.0, 105.2, 110.5, 113.2, 115.0
    ]
}

# Création du DataFrame Pandas à partir du dictionnaire
df = pd.DataFrame(data)

# Création de la figure Plotly
fig = px.line(
    df, 
    x="Année", 
    y="Indice_Prix", 
    markers=True,
    labels={'Année': 'Année', 'Indice_Prix': 'Indice des prix / Pouvoir d\'achat'},
    title="Évolution de l'Indice sur les 30 dernières années"
)

fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='black')
)

# Initialisation de Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Mise en page (avec vos styles personnalisés)
app.layout = html.Div([
    dbc.NavbarSimple(
        brand="Dashboard Économique", 
        color="primary", 
        dark=True, 
        children=[
            dbc.NavLink("Accueil", href="#"),
            dbc.NavLink("Statistiques", href="#"),
        ]
    ),

    html.Header("Rapport Statistiques", style={'borderStyle': 'dotted', 'padding': '10px'}),
    html.H1("Indicateur Économique", style={'color': 'blue', 'textAlign': 'center'}),
    html.H2("Pouvoir d'achat", style={'backgroundColor': 'orange', 'color': 'white', 'padding': '5px'}),
    html.H3("Analyse sur 30 ans", style={'textDecoration': 'green wavy underline'}),
    
    html.Br(),
    html.P("Ce graphique s'appuie sur un dictionnaire converti en DataFrame Pandas.", style={'textAlign': 'center'}),    
    html.Hr(),

    # Intégration du graphique
    html.Div([
        dcc.Graph(figure=fig)
    ], style={'marginLeft': '50px', 'marginRight': '50px'})
])

if __name__ == '__main__':
    app.run(debug=True)