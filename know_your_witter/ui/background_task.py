import threading


class BackgroundTask:

    def __init__(self, task_func_pointer):
        self.__taskFuncPointer_ = task_func_pointer
        self.__workerThread_ = None
        self.__isRunning_ = False

    def task_func_ponter(self):
        return self.__taskFuncPointer_

    def is_running(self):
        return self.__isRunning_ and self.__workerThread_.isAlive()

    def start(self):
        if not self.__isRunning_:
            self.__isRunning_ = True
            self.__workerThread_ = self.WorkerThread(self)
            self.__workerThread_.start()

    def stop(self):
        self.__isRunning_ = False

    class WorkerThread(threading.Thread):
        def __init__(self, bg_task):
            threading.Thread.__init__(self)
            self.__bgTask_ = bg_task

        def run(self):
            try:
                self.__bgTask_.task_func_ponter()(self.__bgTask_.is_running)
            except Exception as e:
                repr(e)
            self.__bgTask_.stop()
