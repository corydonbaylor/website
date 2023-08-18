from flask import render_template
from app import app

# web devlopment routes


@app.route('/tutorials')
def tutorials():
    return render_template('pages/tutorials/tutorials.html', title='Tutorials', pad='p-0', color='greys')


@app.route('/tutorials/linux_git')
def linux_git():
    return render_template('pages/tutorials/build_website/linux_git.html', title='Linux and Git', color='greys')


@app.route('/tutorials/html_css')
def html_css():
    return render_template('pages/tutorials/build_website/html_css.html', title='HTML and CSS', color='greys')


@app.route('/tutorials/bootstrap')
def bootstrap():
    return render_template('pages/tutorials/build_website/bootstrap.html', title='Bootstrap', color='greys')


@app.route('/tutorials/local_raspberry')
def local1():
    return render_template('pages/tutorials/build_website/using_raspberry.html', title='Hosting: Raspberry Pi', color='greys')


@app.route('/tutorials/hello_flask')
def flask1():
    return render_template('pages/tutorials/build_website/Flask.html', title='Flask pt. I: Creating Your First Flask App', color='greys')


@app.route('/tutorials/templates')
def flask2():
    return render_template('pages/tutorials/build_website/templates.html', title='Flask pt. II: Templating with Jinja2', color='greys')


@app.route('/tutorials/local_host_2')
def local2():
    return render_template('pages/tutorials/build_website/local_hosting_2.html', title='Flask and Apache', color='greys')


@app.route('/tutorials/port_forwarding')
def local3():
    return render_template('pages/tutorials/build_website/port_forwarding.html', title='Port Forwarding', color='greys')

# Shiny Routes


@app.route('/tutorials/reactivity')
def reactivity():
    return render_template('pages/tutorials/shiny/reactivity.html', title='Reactivity', color='greys')


@app.route('/tutorials/dashboard')
def dashboard():
    return render_template('pages/tutorials/shiny/dashboard.html', title='shinydashboard', color='greys')


@app.route('/tutorials/modules')
def modules():
    return render_template('pages/tutorials/shiny/modules.html', title='Modules', color='greys')

# Python Routes


@app.route('/tutorials/data_types')
def data_types():
    return render_template('pages/tutorials/python/data_types.html', title='Data Types', color='greys')


@app.route('/tutorials/saving')
def saving():
    return render_template('pages/tutorials/python/save.html', title='Loading and Saving Data', color='greys')


@app.route('/tutorials/pandas')
def pandas():
    return render_template('pages/tutorials/python/pandas.html', title='Pandas', color='greys')


@app.route('/tutorials/filtering')
def filtering():
    return render_template('pages/tutorials/python/filtering.html', title='Filtering', color='greys')


@app.route('/tutorials/combining_data')
def combining_data():
    return render_template('pages/tutorials/python/combining_data.html', title='Combining Data', color='greys')

# docker routes


@app.route('/tutorials/hello_docker')
def hello_docker():
    return render_template('pages/tutorials/docker/hello_docker.html', title='Hello Docker', color='greys')


@app.route('/tutorials/manage_docker')
def manage_docker():
    return render_template('pages/tutorials/docker/manage_docker.html', title='Manage Docker', color='greys')


@app.route('/tutorials/write_docker')
def write_docker():
    return render_template('pages/tutorials/docker/write_docker.html', title='Write Docker', color='greys')


@app.route('/tutorials/docker_swarm')
def docker_swarm():
    return render_template('pages/tutorials/docker/write_docker.html', title='Docker Swarm', color='greys')
