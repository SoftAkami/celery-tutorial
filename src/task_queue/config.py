from enum import Enum, unique


@unique
class QueueName(str, Enum):

    QUEUE0 = "Queue0"
    QUEUE1 = "Queue1"
    QUEUE2 = "Queue2"
