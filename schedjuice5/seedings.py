from django_seed import Seed
from app_users.models import *
from app_finance.models import *
from app_auth.models import *
import random
from django.apps import apps

seeder = Seed.seeder()


def addEntity():
    seeder.add_entity(
        Account,
        3,
        {
            "email": lambda x: seeder.faker.email(),
            "password": lambda x: seeder.faker.password(),
            "is_active": lambda x: True,
            "is_staff": lambda x: False,
            "is_superuser": lambda x: False,
        },
    )

    seeder.add_entity(
        Staff,
        10,
        {
            "name": lambda x: seeder.faker.name(),
            "account": lambda x: random.choice(Account.objects.all()),
        },
    )

    seeder.add_entity(
        Record,
        10,
        {
            "name": lambda x: "Record " + seeder.faker.name(),
            "bank_type": lambda x: random.choice(["KBZ", "AYA", "CB", "KBZ_Pay"]),
        },
    )

    inserted_pks = seeder.execute()
    return inserted_pks


def get_field_value():
    registered_apps = ["app_users", "app_docs", "app_finance", "app_auth"]
    models = []
    for i in registered_apps:
        models += [i for i in apps.get_app_config(i).get_models()]

    for i in models:
        fields = {}
        for j in i._meta.get_fields():
            if j.name == "id":
                continue
            elif j.name == "name":
                fields[j.name] = seeder.faker.name()
            elif j.name in ["email", "secondary_email"]:
                fields[j.name] = seeder.faker.email()
            elif j.name == "password":
                fields[j.name] = seeder.faker.password()
            elif j.get_internal_type() == "BooleanField":
                fields[j.name] = random.choice([True, False])
            elif j.get_internal_type() == "DateTimeField":
                fields[j.name] = seeder.faker.date_time_this_year()
            elif j.get_internal_type() == "IntegerField":
                fields[j.name] = random.randint(1, 100)
            elif j.get_internal_type() == "CharField":
                fields[j.name] = seeder.faker.lorem()

        seeder.add_entity(i, 100, fields)

        inserted_pks = seeder.execute()
        return inserted_pks


def dyamicAddEntity(model, count, **kwargs):
    field_names = [field.name for field in model._meta.get_fields()] + [
        "created_at",
        "updated_at",
    ]
    if kwargs is not None:
        for key in kwargs:
            if key not in field_names:
                raise Exception(f"{key} is not a valid field name for {model}")

    def get_value(field_name):
        if field_name in kwargs:
            return random.choice(kwargs[field_name])
        elif field_name == "name":
            return seeder.faker.name()
        elif field_name == "email":
            return seeder.faker.email()
        elif field_name == "password":
            return seeder.faker.password()
        elif field_name == "is_active":
            return True
        elif field_name == "is_staff":
            return False
        elif field_name == "is_superuser":
            return False
        elif field_name == "created_at" or field_name == "updated_at":
            return seeder.faker.date_time_this_year()
        elif field_name == "id":
            return None
        else:
            return seeder.faker.name()

    seeder.add_entity(model, count, {field: get_value(field) for field in field_names})

    inserted_pks = seeder.execute()
    return inserted_pks
