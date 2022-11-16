import threading, thread_manager

PAGE_LEN = 5 # 5 instructions per page, 15 bytes per instruction, total bytes 15*5
#virtual addr = [pid, page, displacement]
#page_table = {page_frame(0-9):[pid, page, status bit]}

#crear threads
#acomodar private data
#mandarlos a correr con 'run'