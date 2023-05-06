import os
from api import create_app

config = os.getenv('APP_SETTINGS')

app = create_app(config)

if __name__ == "__main__":
    app.run()
