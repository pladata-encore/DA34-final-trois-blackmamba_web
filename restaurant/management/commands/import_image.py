# import_images.py

import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import image paths from a CSV file and print their corresponding URLs'

    def handle(self, *args, **options):
        csv_file_path = r'C:\projects\blackmamba\seongsu_restaurant_final.csv'

        with open(csv_file_path, newline='', encoding='UTF-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Read image file paths from the CSV row
                img_file1 = row['img_file1'] if 'img_file1' in row else None
                img_file2 = row['img_file2'] if 'img_file2' in row else None

                # List to store absolute paths of image files
                absolute_paths = []
                if img_file1:
                    absolute_paths.append(img_file1)
                if img_file2:
                    absolute_paths.append(img_file2)

                # Convert absolute paths to relative paths
                relative_paths = [os.path.relpath(path, settings.MEDIA_ROOT) for path in absolute_paths]

                # Construct URLs to serve the images
                image_urls = [os.path.join(settings.MEDIA_URL, path).replace("\\", "/") for path in relative_paths]

                # Print each image URL
                for image_url in image_urls:
                    self.stdout.write(self.style.SUCCESS(f'Image URL: {image_url}'))
