import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os



class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        # Take any action here when a file is first created.
        path = event.src_path
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print ("Received created event - %s." % path)

        elif event.event_type == 'modified':
            # print("Received mmodified event - %s." % path)
            ext = os.path.splitext(path)[-1].lower()
            if ext == ".html":
                print()
                print(path, "is a html file")
            else:
                print("other file")

        elif event.event_type == 'deleted':
            #Taken any action here when a file is created.
            print ("Recieved Deleted event - %s."  % event.src_path)



def new(path):
    observer = Observer()
    observer.schedule(Handler(), path=path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

def main():
    new()

if __name__ == '__main__':
    main()