import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print (event)


def FileWatch(folderpath):
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, folderpath, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



def main():


 if __name__ == "__main__":
    main()
