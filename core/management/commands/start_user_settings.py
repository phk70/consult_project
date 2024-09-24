from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import Master, Service, Visit

class Command(BaseCommand):
    help = 'Создает тестовые данные для проекта'

    def handle(self, *args, **kwargs):
        # Вывод данных в консоль
        self.stdout.write('Создание суперпользователя...')
        User.objects.create_superuser('admin', 'monin_vladimir@mail.ru', 'admin')


        self.stdout.write('Создание группы модераторов...')
        moderators_group, created = Group.objects.get_or_create(name='Модераторы')

        self.stdout.write('Назначение разрешений для группы модераторов...')
        master_content_type = ContentType.objects.get_for_model(Master)
        service_content_type = ContentType.objects.get_for_model(Service)
        visit_content_type = ContentType.objects.get_for_model(Visit)

        view_master = Permission.objects.get(content_type=master_content_type, codename='view_master')
        view_service = Permission.objects.get(content_type=service_content_type, codename='view_service')
        view_visit = Permission.objects.get(content_type=visit_content_type, codename='view_visit')
        change_visit = Permission.objects.get(content_type=visit_content_type, codename='change_visit')
        add_visit = Permission.objects.get(content_type=visit_content_type, codename='add_visit')

        moderators_group.permissions.add(view_master, view_service, view_visit, change_visit, add_visit)

        self.stdout.write('Загрузка фикстур...')
        dump_path = os.path.join(os.getcwd(), 'dump.json')
        if os.path.exists(dump_path):
            call_command('loaddata', dump_path, verbosity=1)
            self.stdout.write(self.style.SUCCESS('Фикстуры успешно загружены'))
        else:
            self.stdout.write(self.style.WARNING('Файл dump.json не найден в корне проекта'))

            
        self.stdout.write(self.style.SUCCESS('Все операции успешно выполнены'))