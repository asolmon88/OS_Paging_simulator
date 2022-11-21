import threading
from time import sleep
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
    self.pages = ["mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000",\
      "mov $1, %rax000mov $13, %rdx00add %rdx, %rax0mov $14, %rdi00div %rdi0000000"]
    self.page_frames = ["","","","","","","","","",""]
    self.page_table = {0:[-1, -1, 0], 1:[-1, -1, 0], 2:[-1, -1, 0], 3:[-1, -1, 0], 4:[-1, -1, 0],\
      5:[-1, -1, 0], 6:[-1, -1, 0], 7:[-1, -1, 0], 8:[-1, -1, 0], 9:[-1, -1, 0]}
    self.pointer_out = 0


def run(private_data, shared_data):
  #print(f"THREAD....")
  #print("My range:", private_data.page_start, " ,", private_data.page_end)
  private_data.PC[0] = private_data.page_start
  while private_data.PC[0] < private_data.page_end:
    virtual_addr = [private_data.pid, private_data.PC[0], private_data.PC[1]*15]
    print(f"VIRTUAL ADDR = pid: {virtual_addr[0]}, page: {virtual_addr[1]}, disp: {virtual_addr[2]}")
    sleep(3)
    shared_data.page_table_lock.acquire()
    print(f"ESTA TRADUCIENDO EL PROCESO {private_data.pid}")
    physical_addr = translate(shared_data.page_table, virtual_addr)
    print(f"Physical addr: {physical_addr}")
    sleep(3)
    if physical_addr == -1:
      print(f"SALE MARCO DE PAG: {shared_data.pointer_out}")
      shared_data.pointer_out = page_fault(shared_data.page_table, virtual_addr,\
        shared_data.pointer_out, shared_data)
      sleep(3)
      physical_addr = translate(shared_data.page_table, virtual_addr)
      print(f"Physical addr dsps de fault: {physical_addr}")
      sleep(3)
    instruction = get_instruction(shared_data, physical_addr)
    shared_data.page_table_lock.release()
    print(f"THREAD: {private_data.pid}, EXECUTING: {instruction}")
    sleep(3)
    private_data.PC[1] += 1
    if private_data.PC[1] > 4:
      private_data.PC[0] += 1
      private_data.PC[1] = 0

