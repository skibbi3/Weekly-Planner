import os
import json

# Todo
# - Make it use a date class
# - GUI

class Tracker:
    def __init__(self) -> None:
        self.reports = {}
        self.file_path = "./reports.json"
        pass

    def loadJSON(self):
        with open(self.file_path, "r") as file:
            self.reports = json.load(file)

    def saveJSON(self):
        with open(self.file_path, "w") as file:
            json.dump(self.reports, file, indent=4)

    def updateRecord(self, record):
        for record_key in list(record.keys()):
            self.reports[record_key] = record[record_key]
        self.saveJSON()

    def returnRecord(self, date):
        if date in list(self.reports.keys()):
            return self.reports[date]
        else:
            return None


tracker = Tracker()
tracker.loadJSON()
#tracker.updateRecord({"24/06/2024": {"Goals": ["This", "that", "those"], "Reflections": "Yes"}})
#tracker.updateRecord({"25/06/2024": {"Goals": ["This", "that", "those"], "Reflections": "Yes"}})
#tracker.returnRecord("25/06/2024")