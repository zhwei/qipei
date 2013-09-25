import datetime
from haystack import indexes
from qipei.apps.need.models import Need


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    car_type = indexes.CharField(model_attr='car_type')
    short_dsc = indexes.CharField(model_attr='short_dsc')
    long_dsc = indexes.CharField(model_attr='long_dsc')
    created_at = indexes.DateTimeField(model_attr='created_at')

    def get_model(self):
        return Need

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())
