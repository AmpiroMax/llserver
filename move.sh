# #!/bin/bash

# # Script to create a Docker container and move models from home to data directory

# # Define source and destination paths
# SOURCE_DIR="/home/mpatratskiy/work/meta_world/llserver/models"
# DEST_DIR="/data/mapatratskiy/models"

# # Create Docker container with mounted volumes
# echo "Creating Docker container with mounted volumes..."
# docker run --rm -it \
#   -v "$SOURCE_DIR:/source" \
#   -v "$DEST_DIR:/destination" \
#   --name models_mover \
#   ubuntu:latest \
#   bash -c "
#     echo 'Starting file transfer...' && \
#     mkdir -p /destination && \
#     cp -rv /source/* /destination/ && \
#     echo 'File transfer completed successfully!'
#   "

# echo "Models have been moved from $SOURCE_DIR to $DEST_DIR"


#!/bin/bash

# Script to create a Docker container and delete all contents of the models directory

# Define the path to the directory to be cleaned
TARGET_DIR="/home/mpatratskiy/work/meta_world/llserver/models"

# Confirm with the user before proceeding
echo "WARNING: This script will delete all contents of $TARGET_DIR"
read -p "Are you sure you want to proceed? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Operation cancelled."
    exit 1
fi

# Create Docker container to delete the contents
echo "Creating Docker container to clean the directory..."
docker run --rm -it \
  -v "$TARGET_DIR:/target" \
  --name models_cleaner \
  ubuntu:latest \
  bash -c "
    echo 'Starting directory cleanup...' && \
    rm -rf /target/* && \
    echo 'Directory cleanup completed successfully!'
  "

echo "All contents have been removed from $TARGET_DIR"
