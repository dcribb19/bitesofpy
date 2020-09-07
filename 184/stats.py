from csv import DictReader
import os
from urllib.request import urlretrieve
from collections import Counter

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        with open(data) as csvfile:
            reader = DictReader(csvfile)
            return [
                    [row['bite'], row['user'], row['completed']]
                    for row in reader
                    ]

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len(set([row[0] for row in self.rows]))

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len(set([row[0] for row in self.rows if row[2] == 'True']))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len(set([row[1] for row in self.rows]))

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len(set([row[1] for row in self.rows if row[2] == 'True']))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        bites = [row[0] for row in self.rows]
        return int(Counter(bites).most_common(1)[0][0])

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        completed = [row[1] for row in self.rows if row[2] == 'True']
        return Counter(completed).most_common(1)[0][0]
