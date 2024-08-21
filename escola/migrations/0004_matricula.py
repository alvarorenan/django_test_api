# Generated by Django 5.1 on 2024-08-21 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_remove_curso_deleted_at_remove_curso_is_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.curso')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.estudante')),
            ],
        ),
    ]
