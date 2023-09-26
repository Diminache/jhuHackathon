import subprocess
script_paths = ["DiagflowApi.py", "LaymansTermsConverter.py"]

# Run each script in the background
for script_path in script_paths:
    subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
