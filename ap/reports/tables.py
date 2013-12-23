import django_tables2 as tables
from reports.models import TraineeReport

class TraineeTable(tables.Table):
    class Meta:
        model = TraineeReport
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        exclude = ("ID",)