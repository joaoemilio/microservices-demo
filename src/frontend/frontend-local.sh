#/bin/bash

go build -o bin/frontend .
cp -av templates/ static/ .bin/

export PORT=8080
export PRODUCT_CATALOG_SERVICE_ADDR="productcatalogservice:3550"
export CURRENCY_SERVICE_ADDR="currencyservice:7000"
export CART_SERVICE_ADDR="cartservice:7070"
export RECOMMENDATION_SERVICE_ADDR="recommendationservice:8080"
export SHIPPING_SERVICE_ADDR="shippingservice:50051"
export CHECKOUT_SERVICE_ADDR="checkoutservice:5050"
export AD_SERVICE_ADDR="adservice:9555"
export ENV_PLATFORM="gcp"

# Initialize using environment variables:

# Set the service name. Allowed characters: # a-z, A-Z, 0-9, -, _, and space.
# If ELASTIC_APM_SERVICE_NAME is not specified, the executable name will be used.
export ELASTIC_APM_SERVICE_NAME=hipstershop_frontend

# Set custom APM Server URL (default: http://localhost:8200)
export ELASTIC_APM_SERVER_URL=https://e502ba7b9aac4941a32d366eb20628c0.apm.southamerica-east1.gcp.elastic-cloud.com:443

# Use if APM Server requires a token
export ELASTIC_APM_SECRET_TOKEN=fUdDairnKQ5L6CUq8U

export ELASTIC_APM_LOG_LEVEL="trace"

./bin/frontend