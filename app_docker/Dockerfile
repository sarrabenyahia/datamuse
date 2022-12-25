FROM python:3.9
#!/bin/bash


# Install Python dependencies.
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the rest of the codebase into the image
COPY run.py .


ENTRYPOINT [ "python", "run.py"]
