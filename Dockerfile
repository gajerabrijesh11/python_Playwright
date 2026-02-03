# Official Playwright Python image
FROM mcr.microsoft.com/playwright/python:v1.41.0-jammy

# Set working directory
WORKDIR /app

# Copy everything into container
COPY . /app

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install browsers
RUN playwright install --with-deps

# Default command
CMD ["pytest", "-v"]
