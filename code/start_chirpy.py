import sys
from time import sleep
from chirpy.chirpy import app


while True:
    try:
        app.run(host='0.0.0.0', port='8686')
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
        sleep(1)
