### conf.d contains multiple examples of inputs, filters, and outputs

### visuals and curl commands for the pipeline configs:
- **minor error correction**: alert-pipeline and notice-pipeline should both be .conf, not .yml, in the middle portion of this graphic (will update in the future)
- this pipeline splits nested events into separate events, ex. a single array containing two "alert" items becomes two distinct events
![logstash-pipeline-map.png](https://github.com/bonifield/helpers/raw/master/logstash/logstash-pipeline-map.png)
```
curl 127.0.0.1:8080 -H "Content-Type: application/json" --data '{"type":"alert", "rule":[{"name":"badstuff1","sid":1234},{"name":"badstuff2","sid":5678}]}'

curl 127.0.0.1:8080 -H "Content-Type: application/json" --data '{"type":"notice", "rule":[{"name":"oddstuff1","sid":4321},{"name":"oddstuff2","sid":8765}]}'
```

### helpful test commands
```
# check the given config for errors and exit
sudo bin/logstash -f conf.d/someconfig.conf --config.test_and_exit

# manually run logstash but allow live editing of the given config in another windo
sudo bin/logstash -f conf.d/someconfig.conf --config.reload.automatic
```
