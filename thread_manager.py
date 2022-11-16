import threading
from MMU import *
class private_data:
  def __init__(self):
    self.PC = [0,0] # [page, displacement]
    self.pid = -1 # process id (thread id)
    self.page_start = -1 # where the pages for process start
    self.page_end = -1 # where pages for the process ends

class shared_data:
  def __init__(self):
    self.page_table_lock = threading.Lock()
    self.pages = [["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"],\
      ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"]]
    self.page_frames = ["","","","","","","","","",""]
    self.page_table = {0:[-1, -1, 0], 1:[-1, -1, 0], 2:[-1, -1, 0], 3:[-1, -1, 0], 4:[-1, -1, 0],\
      5:[-1, -1, 0], 6:[-1, -1, 0], 7:[-1, -1, 0], 8:[-1, -1, 0], 9:[-1, -1, 0]}


def run(private_data, shared_data):
  pointer_out = 0
  private_data.PC[0] = private_data.page_start
  while private_data.PC[0] < private_data.page_end:
    virtual_addr = [private_data.pid, private_data.PC[0], private_data.PC[1]*15]
    shared_data.page_table_lock().acquire()
    physical_addr = translate(shared_data.page_table, virtual_addr)
    if physical_addr == -1:
      pointer_out = page_fault(shared_data.page_table, virtual_addr,\
        pointer_out, shared_data)
      physical_addr = translate(shared_data.page_table, virtual_addr)
    instruction = get_instruction(shared_data)
    shared_data.page_table_lock().release()
    print(f"THREAD: {private_data.pid}, EXECUTING: {instruction}")
    private_data.PC[1] += 1
    if private_data.PC[1] > 4:
      private_data.PC[0] += 1
      private_data.PC[1] = 0
