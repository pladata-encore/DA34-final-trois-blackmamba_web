import pandas as pd
import csv
from django.core.management.base import BaseCommand
from restaurant.models import Restaurant
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = 'A command to import restaurant data from a CSV file to the database'

    def handle(self, *args, **options):
        csv_file = r'C:\projects\blackmamba\seongsu_restaurant_final.csv'  # CSV 파일 경로를 설정합니다.

        try:
            # 데이터베이스 연결 설정
            engine = create_engine('sqlite:///db.sqlite3')

            # CSV 파일 읽기
            df = pd.read_csv(csv_file)

            # 첫 번째 열이 인덱스일 경우 제거
            if 'Unnamed: 0' in df.columns:
                df = df.drop(columns=['Unnamed: 0'])

            # 데이터베이스에 데이터 삽입
            df.to_sql(Restaurant._meta.db_table, con=engine, if_exists='replace', index=False)
            self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV to database'))

            # CSV 파일에서 직접 데이터 읽어서 Django 모델에 저장
            with open(csv_file, encoding='UTF8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    restaurant = Restaurant(
                        no=row['no'],
                        title=row['title'],
                        local_category=row['local_category'],
                        food_category_1st=row['food_category_1st'],
                        food_category_2nd=row['food_category_2nd'],
                        dining_food_cate_1=row['dining_food_cate_1'],
                        dining_food_cate_2=row['dining_food_cate_2'],
                        information=row['information'],
                        isParking=row['isParking'].lower() in ['true', '1', 't', 'y', 'yes'],
                        isValet=row['isValet'].lower() in ['true', '1', 't', 'y', 'yes'],
                        isPet=row['isPet'].lower() in ['true', '1', 't', 'y', 'yes'],
                        isPackaging=row['isPackaging'].lower() in ['true', '1', 't', 'y', 'yes'],
                        isReservation=row['isReservation'].lower() in ['true', '1', 't', 'y', 'yes'],
                        address=row['address'],
                        phone=row['phone'],
                        menu1=row['menu1'],
                        price1=row['price1'],
                        menu2=row['menu2'],
                        price2=row['price2'],
                        menu_url=row['menu_url'],
                        diningcode_Star=row['diningcode_Star'] if row['diningcode_Star'] else None,
                        diningcode_Score=row['diningcode_Score'] if row['diningcode_Score'] else None,
                        comment=row['comment'] if row['comment'] else None,
                        comment_weight=row['comment_weight'] if row['comment_weight'] else None,
                        rank_score=row['rank_score'] if row['rank_score'] else None,
                        mon_business=row['mon_business'],
                        mon_breaktime=row['mon_breaktime'],
                        tues_business=row['tues_business'],
                        tues_breaktime=row['tues_breaktime'],
                        wed_business=row['wed_business'],
                        wed_breaktime=row['wed_breaktime'],
                        thurs_business=row['thurs_business'],
                        thurs_breaktime=row['thurs_breaktime'],
                        fri_business=row['fri_business'],
                        fri_breaktime=row['fri_breaktime'],
                        sat_business=row['sat_business'],
                        sat_breaktime=row['sat_breaktime'],
                        sun_business=row['sun_business'],
                        sun_breaktime=row['sun_breaktime'],
                        latitude=row['latitude'],
                        longitude=row['longitude'],
                        img_file1=row['img_file1'] if 'img_file1' in row else None,
                        img_file2=row['img_file2'] if 'img_file2' in row else None,
                        closest_parking_name=row['closest_parking_name'],
                        closest_parking_address=row['closest_parking_address'],
                        closest_parking_latitude=row['closest_parking_latitude'],
                        closest_parking_longitude=row['closest_parking_longitude']
                    )
                    restaurant.save()

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
