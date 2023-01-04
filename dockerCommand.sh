# run command to start kafka
docker-compose up -d

# check is kafka is running
docker-compose logs -f kafka

# create topic
docker-compose exec kafka kafka-topics.sh --create --topic delhaize_shop --bootstrap-server localhost:9092

# check if topic has been created
docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092