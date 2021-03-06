# Generated by Django 3.1.4 on 2020-12-04 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201204_1240'),
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changehistory',
            name='executor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.executor'),
        ),
        migrations.AlterField(
            model_name='changehistory',
            name='resolution',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='changehistory',
            name='stage',
            field=models.CharField(choices=[('Created', 'Created'), ('Assigned', 'Assigned to the executer'), ('Paid', 'Payment issued'), ('Returned', 'Returned to the executor'), ('Canceled', 'executor removed from payment'), ('Expired', 'Expired')], default='Created', max_length=10),
        ),
    ]
