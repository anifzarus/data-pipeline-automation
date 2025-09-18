#!/bin/bash

#local file path to log file after every run
LOGFILE="C:/Users/anifz/OneDrive/Desktop/DISS/FinalProject/run_log.txt"

# Python file to upload dataset to azure blob storage
python upload_blob.py

#logging in the notepad file after execution
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Script executed successfully." >> "$LOGFILE"


