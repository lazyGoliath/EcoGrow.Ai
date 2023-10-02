from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('work.html')

@app.route('/submit', methods=['POST'])
def submit():
    crop_type = request.form['crop-type']
    terrain_type = request.form['terrain-type']
    radar_data = request.form['radar-data']
    sensor_data = request.form['sensor-data']

    # Save data to a file
    with open('collected_data.txt', 'w') as file:
        file.write(f"Crop Type: {crop_type}\n")
        file.write(f"Terrain Type: {terrain_type}\n")
        file.write(f"Radar Data:\n{radar_data}\n")
        file.write(f"Sensor Data:\n{sensor_data}\n")

    return render_template('work.html', message="Data submitted and saved as 'collected_data.txt'")

if __name__ == '__main__':
    app.run(debug=True)
