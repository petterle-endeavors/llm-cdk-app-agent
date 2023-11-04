from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import (
    FileSystemEvent,
    FileSystemEventHandler,
)


class MyHandler(FileSystemEventHandler):

    def __init__(
        self,
        indexer: Any,
    ) -> None:
        super().__init__()
        self.indexer = indexer

    def on_any_event(self, event: FileSystemEvent):
        print(f'Event type: {event.event_type}  path : {event.src_path}')
        # TODO: Handle file deletion
        self.indexer.delete_file
        self.indexer.index_file(event.src_path)


def watch_directory(path: Path, indexer: Any) -> None:
    event_handler = MyHandler(indexer)
    observer = Observer()
    observer.schedule(event_handler, path=str(path), recursive=False)
    observer.start()
