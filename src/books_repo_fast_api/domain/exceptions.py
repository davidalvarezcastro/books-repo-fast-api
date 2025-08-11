import attr


@attr.define
class MessageError(Exception):
    message: str


class NotFoundError(MessageError):
    pass
