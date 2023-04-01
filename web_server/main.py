import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')  # Decorator
def get_list():
    return [1, 2, 3, 4]


@app.get('/contact')  # Decorator
def get_list():
    return {'name': 'Platzi'}


@app.get("/html", response_class=HTMLResponse)  # Decorator
def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


def run():
    categories_url = 'https://api.escuelajs.co/api/v1/categories'
    store.get_categories(categories_url)


if __name__ == '__main__':
    print("Starting...")
    run()
