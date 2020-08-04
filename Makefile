build:
	@echo "Build sql-engine in docker."
	docker build -t space-invaders:latest .

run:
	@echo "Run sql-engine in docker."
	docker run -it space-invaders:latest

clean:
	@echo "Clean docker images."
	docker rmi -f space-invaders:latest