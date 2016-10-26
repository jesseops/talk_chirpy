#!/bin/bash
docker stop presentation; docker rm presentation; docker run -v ~/code/talk_chirpy/talk:/slides -p 8000:1948 -d --name presentation jesseops/reveal-md --theme night
