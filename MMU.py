def translate(page_table, virtual_addr):
  pid_page = [virtual_addr[0], virtual_addr[1]]

  for i in range(len(page_table)):
    section = page_table[i]
    if section[0] == pid_page[0] and section[1] == pid_page[1]\
      and section[2] == 1:
      return i
  return -1

def get_instructions(shared_data, virtual_addr, pointer_out):
  shared_data.page_frames[pointer_out] = shared_data.pages[virtual_addr[1]]

def get_instruction(shared_data, virtual_addr):
  return shared_data.page_frames[virtual_addr[1]][virtual_addr[2]:virtual_addr[2]+15]

def page_fault(page_table, virtual_addr, pointer_out, shared_data):
  page_table[pointer_out] = [virtual_addr[0], virtual_addr[1]]
  get_instructions(shared_data, virtual_addr, pointer_out)
  pointer_out = (pointer_out + 1)%10
  return pointer_out
