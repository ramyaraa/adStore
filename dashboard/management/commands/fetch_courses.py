import requests
from django.core.management.base import BaseCommand
from dashboard.models import Course  # Ensure the correct path to your model

class Command(BaseCommand):
    help = 'Fetch courses from API and store them in the database'

    def handle(self, *args, **kwargs):
        base_url = 'https://findmycourse-backend.findmycourse.in/all?page='
        page = 1

        while True:
            response = requests.get(base_url + str(page))
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Error fetching page {page}'))
                break

            data = response.json().get('courses', [])  # Get 'courses' from the response
            if not data:
                self.stdout.write(self.style.SUCCESS('No more data to fetch'))
                break

            for item in data:
                Course.objects.update_or_create(
                    course_id=item['id'],
                    defaults={
                        'title': item['title'],
                        'language': item.get('language', 'Unknown'),
                        'category': item.get('category', 'Unknown'),
                        'course_link': item.get('courseLink', ''),
                        'original_price': item.get('originalPrice', ''),
                        'image_link': item.get('imageLink', ''),
                    }
                )

            self.stdout.write(self.style.SUCCESS(f'Successfully fetched page {page}'))
            page += 1



