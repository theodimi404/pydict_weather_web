from flask import Blueprint, render_template, request
from services import services_predict

api = Blueprint(
    name="controller_predict",
    import_name="controller_predict",
    url_prefix="/home/predict"
)


@api.route('/')
def predict():
    city1 = request.args.get('city', None)
    city = services_predict.main(city1)
    if city:
        return render_template('predict.html', city=city, city1=city1)
    else:
        return render_template('error.html')
