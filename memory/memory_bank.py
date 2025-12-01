import json
from pathlib import Path

class MemoryBank:
    def __init__(self, path='memory/memory_bank.json'):
        self.path = Path(path)
        self.data = {'rules': {}, 'historical': {}}
        if self.path.exists():
            try:
                self.data = json.loads(self.path.read_text())
            except Exception:
                self.data = {'rules': {}, 'historical': {}}

    def update_from_summary(self, summary):
        # store last summary under 'historical' with a simple counter
        hist = self.data.get('historical', {})
        n = len(hist) + 1
        hist[str(n)] = summary
        self.data['historical'] = hist
        self._save()

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2))
