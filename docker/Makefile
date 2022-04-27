.PHONY: build
build:
	#docker build -t cbc-centos-7 	 -f Dockerfiles/centos-7     .
	docker build -t cbc-ubuntu-focal -f Dockerfiles/ubuntu-focal .
	docker build -t cbc-ubuntu-jammy -f Dockerfiles/ubuntu-jammy .

# .PHONY: centos-7 
# centos-7:
# 	docker run -it -u root -v ${PWD}/data:/home/ubuntu/data cbc-centos-7

.PHONY: ubuntu-focal
ubuntu-focal: 
	docker run -it -u root -v ${PWD}/scripts:/scripts cbc-ubuntu-focal

.PHONY: ubuntu-jammy
ubuntu-jammy:
	docker run -it -u root -v ${PWD}/scripts:/scripts cbc-ubuntu-jammy
