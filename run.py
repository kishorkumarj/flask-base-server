import os
from app_server import app


app.run(debug=True, host="0.0.0.0", port=3001)