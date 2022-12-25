#!/bin/bash
echo "Getting data from API: opendata.paris.fr que faire a paris" 
OUTPUT_PATH=$1
curl -X 'GET' \
 'https://opendata.paris.fr/api/v2/catalog/datasets/que-faire-a-paris-/exports/csv?limit=-1&offset=0&lang=fr&timezone=UTC' \
  -H 'accept: */*' > $OUTPUT_PATH

