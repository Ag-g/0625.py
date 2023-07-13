# from threading import Thread
# from multiprocessing import Process
# # def func(name):
# #     for i in range(1000):
# #         print(name, i)
# #
# # if __name__ == "__main__":
# #
# #     t = Thread(target=func)         t = Thread(target=func, args = ("zhou",))  给函数传参数必须是元组
# #     t.start() # 此线程状态为可以开始工作状态，具体执行时间是cpu决定
# #     for i in range(1000):
# #         print("main", i)
#
# class MyThread(Thread):
#     def run(self) -> None: # 线程被执行时，被执行的就是run
#         for i in range(1000):
#             print("子线程", i)
#
# if __name__ == "__main__":
#     t = MyThread()
#     # t.run() 方法的调用，单线程
#     t.start()
#     for i in range(1000):
#         print("主线程", i)

# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(name):
#     for i in range(100):
#         print(name, i)
#
# if __name__ == '__main__':
#     # 创建有50个线程的线程池
#     with ThreadPoolExecutor(50) as t:
#         for i in range(100):
#             t.submit(func, name = f"线程{i}")
#
#     # 等待线程池任务结束之后才继续执行
#     print("123")






