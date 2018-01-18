from bottle import (route, get, post, run, static_file, default_app,
                    jinja2_template as template)


# Expose app for wsgi
app = default_app()


# Routings
@get('/')
def home():
    context = {'message': 'Hello bottle!'}
    return  template('home', context)


@get('/robots.txt')
def robots_txt():
    return static_file('robots.txt', root='static')


@get('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='static')


# Run server for development
if __name__ == '__main__':
    run(host='127.0.0.1', port=3000, debug=True, reloader=True)
