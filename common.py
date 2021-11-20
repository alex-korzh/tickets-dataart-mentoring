from flask import Response as BaseResponse


class Response(BaseResponse):
    default_mimetype = "application/json"
