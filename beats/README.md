manually testing beats (change packetbeat to filebeat, etc)

    sudo packetbeat --path.config /etc/packetbeat/ test config
    sudo packetbeat --path.config /etc/packetbeat/ -e

the Kafka output in `packetbeat.yml` can be used in all of the Beats products (change entries where necessary)
