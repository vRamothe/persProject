# Step 3 of 3: Add unique constraints now that slugs are populated

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_backfill_slugs_gratuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterUniqueTogether(
            name='chapitre',
            unique_together={('matiere', 'niveau', 'ordre'), ('matiere', 'niveau', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='lecon',
            unique_together={('chapitre', 'ordre'), ('chapitre', 'slug')},
        ),
    ]
