import sys
from time import sleep
from chirpy import app


while True:
    try:
        app.run(host='0.0.0.0', port=app.config['PORT'])
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
        sleep(1)
