#!/bin/bash

litestar database upgrade

granian --host 0.0.0.0 --port 8000 --interface asgi app.asgi:app