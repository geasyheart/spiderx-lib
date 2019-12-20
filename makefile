gen-proto:
	@echo "gen-proto"
	python -m grpc_tools.protoc -I ./spiderx_lib/invoke/protos/ --python_out=./spiderx_lib/invoke/gen/ --grpc_python_out=./spiderx_lib/invoke/gen/ ./spiderx_lib/invoke/protos/*
