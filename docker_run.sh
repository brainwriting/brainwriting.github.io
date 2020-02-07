# docker run -it --rm mfekadu/brainwriting \
#     -e api_key \
#     -e spreadsheet_id \
#     -e spreadsheet_range \
#     -e client_id \
#     -e project_id \
#     -e client_secret

# docker run -e api_key -e spreadsheet_id -e client_id -e project_id -e client_secret -it --rm mfekadu/brainwriting


# will be running on http://localhost:8080/
# or whatever is the server IP when deployed
docker run -it --rm -p 8080:8080  mfekadu/brainwriting
