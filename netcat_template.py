#!/usr/bin/env python
from pwn import *

SERVER = "some_server"
PORT = 8080

### run a remote process
s = remote(SERVER, PORT, timeout=9999)
### run a local process
# s = process('./my_program', shell=True)

### interact with it with

# s.recvall()
# s.recvuntil('Message : ')
# s.recvline()

# s.send(msg + '\n')
# s.sendline(msg)

# s.interactive()
