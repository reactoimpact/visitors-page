from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(docs_url=None, redoc_url=None)

counter = 0

@app.get("/", response_class=HTMLResponse)
async def root():
    global counter
    counter += 1

    return f"""
    <html>
        <head>
            <style>
                /* hello there */
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }}
                .counter {{
                    font-size: 48px;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="counter">{counter} visitors.</div>
        </body>
    </html>
    """