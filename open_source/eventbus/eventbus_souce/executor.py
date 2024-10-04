import abc
import queue
import threading


class PendingPost:

    def __init__(self, subscription, event):
        self.subscription = subscription
        self.event = event


class Executor(abc.ABC):
    """
    每个订阅者都会有一个线程模式，线程模式决定其订阅方法运行在哪个线程中，这几种线程模式，分别为：
    - `POSTING`：默认的线程模式，在哪个线程发送事件就在对应的线程处理事件。
    - `MAIN`：如果是在主线程发送事件，直接在主线程处理事件。反之，如果在子线程中发送事件，则需要切换到主线程来处理事件。(在 Android 中使用比较多)
    - `MAIN_ORDERED`：不管在哪个线程发送事件，都会将事件入队列，在主线程上有序执行。
    - `BACKGROUND`：如果是在子线程中发送事件，则直接在该子线程中处理事件。反之，如果是在主线程中发送事件，则需要将该事件入消息队列，
                    切换到子线程，用线程池来有序处理该事件。（如果不是 Android 中使用，总是使用该模式）-- 最优的线程池解法
    - `ASYNC`：无论是在哪个线程发送事件，都会将该事件入消息队列，通过线程池在子线程上处理事件。
               如果订阅者方法的执行可能需要一些时间 (如网络访问)，则应使用此模式。
    """
    @abc.abstractmethod
    def enqueue(self, subscription, event):
        pass


class MainExecutor(Executor):

    def __init__(self, eventbus):
        self.bus = eventbus

    def enqueue(self, subscription, event):
        self.bus.invoke_subscriber(subscription, event)


class MainOrderExecutor(Executor):
    """
    不管在哪个线程发送事件，都会将事件入队列，在主线程上有序执行
    """
    def __init__(self, eventbus):
        self.quit = False
        self.queue = queue.Queue()
        self.bus = eventbus
        # 修复executor未设置为后台运行模式导致阻塞主线程的bug
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def enqueue(self, subscription, event):
        pending_post = PendingPost(subscription, event)
        self.queue.put(pending_post)

    def run(self):
        while not self.quit:
            pending_post = self.queue.get()
            self.bus.invoke_subscriber(pending_post.subscription, pending_post.event)

    def stop(self):
        self.quit = True
