#!/bin/bash

set -x

# Go to the root
cd "${0%/*}" || exit 1

# 1. Work only with the latest master. Releasing from another branch is not supported.
git checkout master
git pull

# 2. Get the latest tag in the repository.
tag=$(git describe --abbrev=0 --tags)
git checkout $tag
ecr_prefix="057506459946.dkr.ecr.eu-central-1.amazonaws.com"
container_tag="$ecr_prefix/uvu:$tag"

# 3. Check, whether it exists in ECR.
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin "$ecr_prefix"
aws ecr describe-images --repository-name="uvu" --image-ids="imageTag=$tag"
if [ $? == 0 ]; then
    echo "The tag $tag is in use in ECR!"
    exit 1
fi

# 4. Build a new image.
cd ../..
docker build -f deployment/docker/django/Dockerfile . -t "${container_tag}"

# 5. Push the builded image to ECR.
docker push "$container_tag"
