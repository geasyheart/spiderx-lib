# coding=utf-8


from concurrent import futures
import logging

import grpc

from spiderx_lib.invoke.gen import task_pb2_grpc, task_pb2


class TaskServiceService(task_pb2_grpc.TaskServiceServicer):

    def SendTaskByClient(self, request, context):
        print(f"policy: {request.policy}")
        print(f"url: {request.url}")
        print(f"site_name: {request.site_name}")
        print(f"depth: {request.depth}")
        print(f"father: {request.father}")
        print(f"task_type: {request.task_type}")
        print(f"dont_filter: {request.dont_filter}")
        print(f"task_id: {request.task_id}")
        print(f"stat: {request.stat}")
        print(f"message: {request.message}")
        return task_pb2.ReplyTaskResponse(err_code=0, message="")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskServiceServicer_to_server(TaskServiceService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
