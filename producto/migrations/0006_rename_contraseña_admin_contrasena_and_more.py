# Generated by Django 4.2.7 on 2023-11-20 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_alter_admin_correo_alter_usuarios_correo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='Contraseña',
            new_name='Contrasena',
        ),
        migrations.RenameField(
            model_name='usuarios',
            old_name='Contraseña',
            new_name='Contrasena',
        ),
    ]
