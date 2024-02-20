#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import daemon
from daemon import runner

class App():
   def __init__(self):
      self.stdin_path      = '/dev/null'
      self.stdout_path     = '/dev/tty'
      self.stderr_path     = '/dev/tty'
      self.pidfile_path    =  '/var/run/test.pid'
      self.pidfile_timeout = 5

   def run(self):
      i = 0
      while True:
         i += 1
         logger.info("message "+i)
         time.sleep(1)

if __name__ == '__main__':
   app = App()
   logger = logging.getLogger("testlog")
   logger.setLevel(logging.INFO)
   formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
   handler = logging.FileHandler("/var/log/test.log")
   handler.setFormatter(formatter)
   logger.addHandler(handler)

   serv = runner.DaemonRunner(app)
   serv.daemon_context.files_preserve=[handler.stream]
   serv.do_action()