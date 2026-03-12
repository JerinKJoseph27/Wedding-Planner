from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enqry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=250)),
                ('p_email', models.EmailField(max_length=254)),
                ('p_phone', models.CharField(max_length=14)),
                ('p_when', models.DateField()),
                ('p_events', models.CharField(max_length=100)),
            ],
        ),
    ]
