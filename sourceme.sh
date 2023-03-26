ME=$(readlink -f "${BASH_SOURCE:-$0}")
export PROJECT_DIR=$(dirname $ME)
export PYTHONPATH=${PYTHONPATH}:${PROJECT_DIR}/src
#export GOOGLE_APPLICATION_CREDENTIALS='<YOUR_GCP_CREDENTIAL_JSON_PATH>'
export GOOGLE_APPLICATION_CREDENTIALS='/home/danh/workspace/self-study/eu-airbnb/cred/dtc-airbnb-33c84c172b76.json'
