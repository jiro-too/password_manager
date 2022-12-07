#! /bin/sh

rm -rfv venv/lib/python3.10/site-packages/*-linux-x86_64.egg *.egg-info build dist 
python3 ./src_p/setup.py install
python3 ./src_p/test.py
