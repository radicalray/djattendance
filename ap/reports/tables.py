import django_tables2 as tables
from accounts.models import Trainee

class TraineeTable(tables.Table):
    class Meta:
        model = Trainee
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}