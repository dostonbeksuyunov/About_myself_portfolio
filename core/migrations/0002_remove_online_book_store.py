from django.db import migrations


def remove_book_store(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug='online-book-store').delete()


class Migration(migrations.Migration):
    dependencies = [('core', '0001_initial')]
    operations = [migrations.RunPython(remove_book_store, migrations.RunPython.noop)]
