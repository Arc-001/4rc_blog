#!/bin/bash

echo "Testing for the venv"

if ! [[ -d venv ]]
then
	echo " Alert]  Venv not present, initiating the first startup"
	
	echo "Adding executing permissions to setup.sh"
	chmod +x setup.sh

	echo "Setup initiated"
	./setup.sh
fi


. venv/bin/activate

python3 api.py
