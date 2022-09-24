from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from core.models import Excel, DataSet, DataInstance
from decimal import Decimal
import openpyxl


@receiver(post_save, sender=Excel, dispatch_uid="after_creation")
def after_creation(sender, instance: Excel, created, **kwargs):
    excel = instance
    if not created:
        return

    wb = openpyxl.load_workbook(excel.data.file, read_only=True)
    for sheet_name in wb.get_sheet_names():
        ws = wb.get_sheet_by_name(sheet_name)
        identifier_dataset = {}
        for row in ws.iter_rows(min_row=2, values_only=True):
            if len(row) == 0 or row[0] is None:
                continue
            identifier = row[3]
            if identifier not in identifier_dataset:
                identifier_dataset[identifier] = DataSet.objects.create(identifier=identifier)
            dataset = identifier_dataset[identifier]
            DataInstance.objects.create(
                lat=Decimal(row[0]),
                lng=Decimal(row[1]), alt=Decimal(row[2]), identifier=row[3], timestamp=int(row[4]),
                                        floor=row[5] if row[5] != "null" else None, horizontal_accuracy=Decimal(row[6]),
                                        vertical_accuracy=Decimal(row[7]), confidence=Decimal(row[8]), activity=row[9], data_set=dataset)
