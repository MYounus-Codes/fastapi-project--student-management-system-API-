# Use Python 3.12 as base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies directly
RUN pip install --no-cache-dir fastapi[standard]>=0.128.0 python-dotenv>=1.2.1 streamlit>=1.52.2 uvicorn>=0.40.0

# Expose ports for backend and frontend
EXPOSE 8000 8501

# Create a startup script to run both services
RUN echo '#!/bin/bash\n\
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &\n\
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0\n\
' > /app/start.sh && chmod +x /app/start.sh

# Run the startup script
CMD ["/bin/bash", "/app/start.sh"]
