
import os
import sys

if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding("utf8")

from app import create_app

config_name = os.getenv("FLASK_CONFIG")
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
