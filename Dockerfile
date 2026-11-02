# (1) Choose a base image
FROM python:3.12-slim
                    
# (2) Set the working directory 
WORKDIR /app

# (3) Copy the dependencies file to the working directory
COPY requirements.txt .

# (4) Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# (5) Copy the rest of the application code
COPY . .

#(6) Specify the command to run the application
CMD ["python", "BasicPythonFile.py"]
