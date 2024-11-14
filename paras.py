import re

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

# Example usage
file_path = r'D:\Python\Flask\Flask Project 2 - Office_Vishwa_Monitoring\moniapp\server_metrix.txt'
metrics = parse_server_metrics(file_path)
print(metrics)