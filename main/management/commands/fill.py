from django.core.management import BaseCommand
from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Фрукты', 'description': '1 уровень'},
            {'name': 'Игры', 'description': '2 уровень'},
            {'name': 'Одежда', 'description': '3 уровень'},
            {'name': 'Техника', 'description': '4 уровень'},
            {'name': 'Книги', 'description': '5 уровень'},
        ]

        # for category_item in category_list:
        #     Category.objects.create(**category_item)

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)