import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/aadit/OneDrive/Desktop/Project102/Downloads"

#Event Handler
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f'Hey, {event.src_path} has been created!')

    def on_modified(self,event):
        print(f'Hey, {event.src_path} has been modified!')

    def on_moved(self,event):
        print(f'Hey, {event.src_path} has been moved!')        

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")   

#Initialize Event Handler Class
event_handler = FileMovementHandler()

#Initialize Observer
observer = Observer()

#Schedule the observer
observer.schedule(event_handler, from_dir, recursive=True)

#Start the observer
observer.start()

#Stop the observer program when any key is pressed
try:
    while True:
        time.sleep(2)
        print('running...')
except KeyboardInterrupt:
    print('Stopped!')
    observer.stop()        
