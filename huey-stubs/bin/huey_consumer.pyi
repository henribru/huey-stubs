from huey.consumer import Consumer as Consumer
from huey.consumer_options import (
    ConsumerConfig as ConsumerConfig,
    OptionParserHandler as OptionParserHandler,
)
from huey.utils import load_class as load_class

def err(s) -> None: ...
def load_huey(path): ...
def consumer_main() -> None: ...
