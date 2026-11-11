from django.db import migrations

REMOVED = ['tashkent-3d-residence', 'bahober', 'yuridik-yordam', 'shajara', 'language-bot', 'buy-a-ticket-bot', 'gym-management', 'hunarmandlar-tarmogi', 'umumiy-sayt', 'u13-task-manager', 'normativ-drf', 'stadium-booking', 'taxi-trips']


def remove_projects(apps, schema_editor):
    apps.get_model('core', 'Project').objects.filter(slug__in=REMOVED).delete()


class Migration(migrations.Migration):
    dependencies = [('core', '0002_remove_online_book_store')]
    operations = [migrations.RunPython(remove_projects, migrations.RunPython.noop)]
