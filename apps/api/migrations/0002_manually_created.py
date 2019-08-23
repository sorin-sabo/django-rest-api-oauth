# Manually created on 2019-08-22 18:20

from django.db import migrations


# noinspection PyUnusedLocal,PyPep8Naming
def add_guest_user(apps, schema_editor):
    User = apps.get_model('api', 'User')
    guest_user = {
        'name': 'Guest',
        'surname': 'User',
        'status': True,
        'email': 'guest@guest.com'
    }

    user = User(**guest_user)
    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_guest_user),
    ]
