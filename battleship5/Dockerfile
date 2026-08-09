# Multi-stage Dockerfile for Angular application
# Builder stage
FROM node:20-alpine AS builder
WORKDIR /app

# Install dependencies based on package.json and package-lock.json (or npm-shrinkwrap.json)
COPY package*.json ./
RUN npm ci

# Copy the rest of the source code and build the Angular app
COPY . ./
RUN npm run build -- --output-path=dist/battleship5 --configuration=production

# Runtime stage using nginx to serve the built files
FROM nginx:alpine
# Remove default nginx static assets
RUN rm -rf /usr/share/nginx/html/*
# Copy built assets from builder stage
COPY --from=builder /app/dist/battleship5 /usr/share/nginx/html
# Expose port 80 for the web server
EXPOSE 80
# Start nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
