# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import task_pb2 as task__pb2


class TaskServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendTaskByClient = channel.unary_unary(
        '/task.TaskService/SendTaskByClient',
        request_serializer=task__pb2.SendTaskRequest.SerializeToString,
        response_deserializer=task__pb2.ReplyTaskResponse.FromString,
        )


class TaskServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendTaskByClient(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendTaskByClient': grpc.unary_unary_rpc_method_handler(
          servicer.SendTaskByClient,
          request_deserializer=task__pb2.SendTaskRequest.FromString,
          response_serializer=task__pb2.ReplyTaskResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'task.TaskService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
