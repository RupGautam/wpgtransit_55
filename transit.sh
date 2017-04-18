curl -s 'https://api.winnipegtransit.com/v2/stops/50536/schedule.json?api-key=<key>' | jq -C '."stop-schedule"."route-schedules"[]."scheduled-stops"[]."times".arrival.scheduled' | sed -n 's/^.*T//p;' | sed 's/"//g' | head -2
