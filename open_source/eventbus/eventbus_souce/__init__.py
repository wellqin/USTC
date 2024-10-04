from .subscribe import Subscribe
from contextvars import ContextVar
from .eventbus import EventBus
bus: ContextVar[EventBus] = ContextVar('bus', default=EventBus())

# most star : https://github.com/seanpar203/event-bus
# current: 调用规范 由于设计时考虑到可能会存在多个实例的情况，故使用ContextVar来包装EventBus实例方便使用者调用。
# https://github.com/cyclegen/eventbus-py
