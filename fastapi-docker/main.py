from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_server_msg():
    return {'Message':'Message from fast api server'}

@app.get('/health')
def health_check():
    return {'Health':'ok'}