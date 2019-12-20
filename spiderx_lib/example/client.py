# coding=utf-8

from spiderx_lib.invoke.services import grpc_service


if __name__ == '__main__':
    grpc_service.open_channel(options={
        "GRPC_URI": "127.0.0.1:50051"
    })

    response = grpc_service.task_service.send_task(
        policy="list",
        url="www.baidu.com",
        site_name="baidu",
        depth=1,
        father="",
        task_type="list",
        message="msg"
    )
    print(response.err_code, response.message)
