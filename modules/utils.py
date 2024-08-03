from datetime import datetime

def log_error(message):
    with open('d:\Omar\Documents\CODERHOUSE\Data Engineering\log\error.log', 'a') as f:
        f.write(f"{datetime.now()}: {message}\n")