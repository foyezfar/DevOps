# Use the official Node.js image as the base image
FROM node:alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the content of the local src directory to the working directory
COPY . .

# Build the React app
RUN npm run build

# Expose port 3000 to the outer world
EXPOSE 3000

# Command to run the React app
CMD ["npm", "start"]
