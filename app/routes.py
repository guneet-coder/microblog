from app import app
@app.route('/')
@app.route('/index')
def index():
    return '''<html>
<head><title>Guneet</title>'''



