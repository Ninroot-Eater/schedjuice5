from schedjuice5.serializers import BaseSerializer
from app_finance.models import Record


class RecordSerializer(BaseSerializer):
    class Meta:
        model = Record