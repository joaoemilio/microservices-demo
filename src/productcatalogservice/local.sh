#/bin/bash

go build -o bin/productcatalogservice .
cp -av products.json ./bin/

export PORT="3550"

# Initialize using environment variables:

# Set the service name. Allowed characters: # a-z, A-Z, 0-9, -, _, and space.
# If ELASTIC_APM_SERVICE_NAME is not specified, the executable name will be used.
export ELASTIC_APM_SERVICE_NAME=hipstershop-productcatalog

# Set custom APM Server URL (default: http://localhost:8200)
export ELASTIC_APM_SERVER_URL=https://e502ba7b9aac4941a32d366eb20628c0.apm.southamerica-east1.gcp.elastic-cloud.com:443

# Use if APM Server requires a token
export ELASTIC_APM_SECRET_TOKEN=fUdDairnKQ5L6CUq8U

./bin/productcatalogservice