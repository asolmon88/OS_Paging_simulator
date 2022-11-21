import threading, thread_manager

PAGE_LEN = 5 # 5 instructions per page, 15 bytes per instruction, total bytes 15*5
#virtual addr = [pid, page, displacement]
#page_table = {page_frame(0-9):[pid, page, status bit]}

shared_data = thread_manager.shared_data()
thread_count = 4
threads = []

for thread_num in range(4) :
  private_data = thread_manager.private_data()
  private_data.pid = thread_num
  private_data.page_start = thread_num * 5
  private_data.page_end = private_data.page_start + 4
  thread = threading.Thread(target=thread_manager.run, args=(private_data,shared_data))
  threads.append(thread)
  thread.start()

for num in range(thread_count):
  threads[num].join()

print("Job done...")