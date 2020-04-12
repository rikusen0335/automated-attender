#!/bin/bash

if [ $# -ne 3 ]; then
  echo "You need 3 arguments." 1>&2
  exit 1
fi

TOKEN=$1
CHANNEL=$2
MSG=$3

echo "Token: ${TOKEN}"
echo "Channel: ${CHANNEL}"
echo "Message: ${MSG}"

RANDUM_NUM=$(echo $RANDOM % 500 + 1 | bc)
echo $RANDUM_NUM
sleep $RANDUM_NUM

curl --location --request POST "https://slack.com/api/chat.postMessage" \
  --header "Content-Type: application/json;charset=UTF-8" \
  --header "Authorization: Bearer ${TOKEN}" \
  --data-raw '{
  "channel": "'"${CHANNEL}"'",
  "text": "'"${MSG}"'",
  "as_user": true
}'
