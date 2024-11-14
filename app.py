from flask import Flask, render_template
import re

app = Flask(__name__)

def parse_server_metrics(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    metrics = {'Server Metrics': [], 'Login Count': [], 'Thread Count': []}
    current_section = None
    
    for line in lines:
        if "Server Metrics" in line:
            current_section = 'Server Metrics'
        elif "Login Count" in line:
            current_section = 'Login Count'
        elif "Thread Count" in line:
            current_section = 'Thread Count'
        elif current_section and re.match(r'^\d', line.strip()):
            metrics[current_section].append(line.strip())
            
    return metrics

@app.route('/')
def home():
    metrics = parse_server_metrics('server_metrix.txt')
    return render_template('index.html', metrics=metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)