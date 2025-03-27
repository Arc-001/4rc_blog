#!/bin/bash


##############################################
# Author Arc
#
#
# note: I know it is a dramtic startupp but I love it
#
#
# ############################################
echo "============Makeing a venv================"

python3 -m venv venv

echo "=========== source into venc=============="

source venv/bin/activate

echo "=========== installing requirements==========="

python3 pip install -r requirements.txt

echo "=========== Starting the api================="

echo "===========changeing executable permissions============="
chmod +x startup.sh

echo "=============Initiating startup================="
./startup.sh


