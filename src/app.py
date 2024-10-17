from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Загрузка модели из папки models
model_path = os.path.join(os.path.dirname(__file__), '../models/linear_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    # Отображение HTML формы
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Получаем данные из формы (если через HTML) или из JSON (если через API)
    if request.form:
        height = float(request.form['height'])
    else:
        data = request.get_json()
        height = float(data['height'])

    # Предсказание на основе модели
    prediction = model.predict([[height]])

    # Если запрос через HTML, вернём результат на страницу
    if request.form:
        return render_template('index.html', prediction_text=f"Предсказанный вес: {prediction[0]:.2f} кг")

    # Если запрос через API, возвращаем JSON
    return jsonify({'predicted_weight': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
