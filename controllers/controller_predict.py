from flask import Blueprint, render_template, request
from services import services_predict

api = Blueprint(
    name="controller_predict",
    import_name="controller_predict",
    url_prefix="/home/predict"
)


@api.route('/')
def predict():
    city_of_choice = request.args.get('city', None)
    # Call the main function from services_predict to find the prediction
    prediction = services_predict.main(city_of_choice)
    if prediction:
        return render_template('predict.html', prediction=prediction, city=city_of_choice)
    else:
        return render_template('error.html')
