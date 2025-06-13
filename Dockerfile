FROM python:3.10-alpine

# Install required tools
RUN apk add --no-cache git curl unzip

# Install Bandit
RUN pip install bandit

# Download and install Gitleaks
RUN curl -sSL https://github.com/gitleaks/gitleaks/releases/download/v8.27.0/gitleaks_8.27.0_linux_x64.tar.gz \
    -o gitleaks.tar.gz && \
    tar -xzf gitleaks.tar.gz && \
    mv gitleaks /usr/local/bin/gitleaks && \
    chmod +x /usr/local/bin/gitleaks && \
    rm gitleaks.tar.gz

# Install Trivy
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Copy code
COPY . /code
WORKDIR /code

# Run the scanner script
ENTRYPOINT ["python", "/code/run_scanners.py"]
