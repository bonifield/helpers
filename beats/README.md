# Beats

## Most of this information comes from the companion repository for [Data Engineering for Cybersecurity](https://nostarch.com/data-engineering-cybersecurity)

## Testing Commands
```
./filebeat test config
./filebeat test output
# or specify another directory
./filebeat --path.config /etc/filebeat/ test config
```

for easier testing, reload modules every second inside `filebeat.yml`
```
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: true
  reload.period: 1s
```

## Manually Running Beats
```
./filebeat -e
# with jq
./filebeat -e 2>&1 | jq '.["message"]'
```

## Keystores
```
./filebeat keystore add --force MY_KEY_PASSPHRASE
# in filebeat.yml for a TLS key passphrase
ssl.key_passphrase: %{MY_KEY_PASSPHRASE}
```

## Modules
modules are in the appropriate Beats directory, then `modules.d/<module>.yml.disabled`

list, then enable
```
sudo filebeat modules list
sudo filebeat modules enable <module>
```

then edit the `<module>.yml` config (now, minus the .disabled extension)

## Packetbeat - Enable Process Monitoring
add to `packetbeat.yml`
```
packetbeat.procs.enabled: true
```

## Dashboards

in `filebeat.yml` or the appropriate Beats configuration
```
setup.kibana:
  host: "https://kibana.local:5601"
  ssl.enabled: true
  ssl.verification_mode: none
  ssl.certificate_authorities: ["<ca-chain>"]
  ssl.certificate: "<cert>"
  ssl.key: "<private-key>"
  ssl.key_passphrase: "abcd1234"
  protocol: "https"
  username: "elastic"
  password: "abcd1234"
```

run the `setup` subcommand to add dashboards and visualizations
```
./filebeat setup --dashboards
```

## Configure ILM and Ingest Pipelines
```
./filebeat setup --pipelines -e
./filebeat setup --pipelines --index-management
```

## Inputs

### Filestream

```
filebeat.inputs:

# reads local files from custom recon tooling
- type: filestream
  id: recon-logs
  enabled: false
  paths:
    - /home/j/example-logs/subfinder*.json
    - /home/j/example-logs/httpx*.json
  parsers:
    - ndjson:
        target: "processed"
        add_error_key: true
  fields_under_root: true
  fields:
    threat.tactic.name: "Reconnaissance"
    threat.tactic.id: "TA0043"
    threat.technique.name: "Gather Victim Network Information"
    threat.technique.id: "T1590"

# see also the system module
- type: filestream
  id: local-syslog-files
  enabled: false
  paths:
    - /var/log/*.log
  exclude_lines: ['.*UFW.*']
  parsers:
    - syslog:
        format: auto
        add_error_key: true

# Windows filestream
# Input that reads Edge update logs
- type: filestream
  enabled: true
  id: edgeupdate-logs
  paths:
    - C:/ProgramData/Microsoft/EdgeUpdate/Log/*.log
    # more files here (NOT event logs)
  encoding: utf-16le-bom
```

### Kafka

plaintext
```
- type: kafka
  enabled: false
  hosts:
    - kafka01:9092
    - kafka02:9092
  topics: [ "filebeat" ]
  group_id: "filebeat"
  tags: [ "from-kafka" ]
  # parse the JSON string in the "message" field, into "processed" nested fields
  parsers:
    - ndjson:
        message_key: "message"
        target: "processed"
        overwrite_keys: true
        add_error_key: true
```

### Redis
```
```

## Outputs

### Logstash

```
output.logstash:
  enabled: true
  hosts: [ "logstash.local:5044" ]
  ssl.enabled: true
  ssl.verification_mode: full
  ssl.certificate: "<cert>"
  ssl.key: "<private-key>"
  ssl.certificate_authorities:
    - <ca-chain>
```

### Kafka

```
output.kafka:
  enabled: true
  hosts: [ "kafka01:9092", "kafka02:9092" ]
  topic: "filebeat"
  client_id: "my-awesome-server-running-filebeat"
  ssl.enabled: true
  ssl.verification_mode: full
  ssl.certificate: "<cert>"
  ssl.key: "<private-key>"
  ssl.certificate_authorities:
    - <ca-chain>
  # optional Kafka headers
  headers:
    - key: "category"
      value: "remoteaccess"
      when:
        equals:
          event.dataset: "zeek.ssh"
    - key: "category"
      value: "web"
      when:
        equals:
          event.dataset: "zeek.tls"
```

### Redis

```
output.redis:
  enabled: true
  hosts: ["localhost"]
  password: "<your-redis-password>"
  key: "filebeat"
  # optionally route using keys (plural) using conditionals
  keys:
    - key: "remoteaccess"
      when:
        or:
          - contains:
              event.dataset: "zeek.ssh"
          - contains:
              event.dataset: "zeek.telnet"
        and:
          - equals:
              event.module: "zeek"
```

### File

```
output.file:
  enabled: true
  path: /var/log/filebeat/
  # Filebeat adds the extension .ndjson; the default filename is set to the Beat name (per documentation)
  filename: threatintel
  permissions: 0640
```

## Custom Processors

```
processors:

  # remove unwanted fields
  - drop_fields:
      # you can't drop event.original nor metadata fields that start with "@"
      fields: ["ecs", "agent.id", "agent.ephemeral_id"]
      when:
        # single conditional
        #equals:
        #  log.file.path: "/home/j/example-logs/httpx-owasp.org.json"
        # multiple conditionals
        or:
          - equals:
              log.file.path: "/home/j/example-logs/httpx-owasp.org.json"
          - equals:
              log.file.path: "/home/j/example-logs/subfinder-owasp.org.json"

  # fix a nested timestamp
  - script:
      lang: javascript
      # example
      # 2099-04-27T22:37:12.463504006-05:00
      #          | 10         |23    |29
      source: >
        function process(event) {
          var t = event.Get("processed.timestamp")
          var front = t.slice(0, 23)
          var back = t.slice(29)
          var combined = front+back
          event.Put("processed.timestamp_fixed", combined)
        }
      when:
        has_fields: [ "processed.timestamp" ]

  # use as document timestamp, instead of "now" time
  - timestamp:
      field: "processed.timestamp_fixed"
      layouts:
        - '2006-01-02T15:04:05.999-07:00'
      test:
        - '2099-04-27T22:37:12.463-05:00'
      when:
        has_fields: [ "processed.timestamp_fixed" ]

  # overwrite or redact given fields
  - script:
      lang: javascript
      source: >
        function process(event) {
          event.Put("user.name", "AnonymizedBankUser")
        }
      when:
        has_fields: [ "user.name" ]
```
