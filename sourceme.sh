ME=$(readlink -f "${BASH_SOURCE:-$0}")
export PROJECT_DIR=$(dirname $ME)

if [[ -z "${GOOGLE_APPLICATION_CREDENTIALS}" ]]; then
  echo "${GOOGLE_APPLICATION_CREDENTIALS} is not defined"
  return 1
fi

DBT_PROFILE=${PROJECT_DIR}/airbnb/dbt/airbnb/profiles.yml
sed -i -r "s|keyfile: (.*)|keyfile: ${GOOGLE_APPLICATION_CREDENTIALS}|g" ${DBT_PROFILE}
