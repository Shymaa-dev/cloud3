import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.routes import app

if __name__ == "__main__":
    app.run(debug=True)
