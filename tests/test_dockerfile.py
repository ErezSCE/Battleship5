import pathlib

def test_dockerfile_contents():
    dockerfile_path = pathlib.Path('battleship5/Dockerfile')
    assert dockerfile_path.is_file(), "Dockerfile should exist at battleship5/Dockerfile"
    content = dockerfile_path.read_text()
    # Check for builder stage using node
    assert 'FROM node:20-alpine AS builder' in content
    # Ensure npm ci is used to install dependencies
    assert 'RUN npm ci' in content
    # Ensure Angular build command is present
    assert 'npm run build' in content
    # Check for runtime stage using nginx
    assert 'FROM nginx:alpine' in content
    # Ensure port 80 is exposed
    assert 'EXPOSE 80' in content
