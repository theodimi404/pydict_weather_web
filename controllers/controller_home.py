from flask import Blueprint, render_template, redirect, url_for, request

api = Blueprint(
    name="controller_home",
    import_name="controller_home",
    url_prefix="/home"
)


@api.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        return redirect(url_for('controller_predict.predict', city=city))
    return render_template('home.html')
