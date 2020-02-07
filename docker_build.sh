# docker build -t mfekadu/brainwriting . \
#      --build-arg api_key \
#      --build-arg spreadsheet_id \
#      --build-arg spreadsheet_range \
#      --build-arg client_id \
#      --build-arg project_id \
#      --build-arg client_secret

# automatically pass in local environment variables into the docker thing
docker build --build-arg api_key --build-arg spreadsheet_id --build-arg spreadsheet_range --build-arg client_id --build-arg project_id --build-arg client_secret -t mfekadu/brainwriting .
