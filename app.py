from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
  
    map = folium.Map(location=[-8.047562, -34.877], zoom_start=10)

    
    areas_de_risco = [
        {"nome": "Área 1", "coords": [-8.047562, -34.877]},
        {"nome": "Área 2", "coords": [-8.052562, -34.870]}
    ]

  
    for area in areas_de_risco:
        folium.Marker(
            location=area["coords"],
            popup=f"<b>{area['nome']}</b>",
            icon=folium.Icon(color='red')
        ).add_to(map)

   
    map.save('templates/map.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

