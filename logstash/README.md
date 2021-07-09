### test curl commands
```
curl 127.0.0.1:8080 -H "Content-Type: application/json" --data '{"type":"alert", "rule":[{"name":"badstuff1","sid":1234},{"name":"badstuff2","sid":5678}]}'

curl 127.0.0.1:8080 -H "Content-Type: application/json" --data '{"type":"notice", "rule":[{"name":"oddstuff1","sid":4321},{"name":"oddstuff2","sid":8765}]}'
```

### visual layout of Logstash pipeline configs
![logstash-pipeline-map.png](https://github.com/bonifield/helpers/raw/master/logstash/logstash-pipeline-map.png)

### helpful test commands
```
# check the given config for errors and exit
sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/someconfig.conf --config.test_and_exit

# manually run logstash but allow live editing of the given config
sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/someconfig.conf --config.reload.automatic
```
