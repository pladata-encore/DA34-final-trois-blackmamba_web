# Generated by Django 4.0.3 on 2024-06-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False, verbose_name='no')),
                ('title', models.CharField(max_length=30, verbose_name='상호명')),
                ('local_category', models.CharField(max_length=20, verbose_name='지역')),
                ('food_category_1st', models.CharField(blank=True, default='한식', max_length=10, verbose_name='음식 카테고리 대형')),
                ('food_category_2nd', models.CharField(blank=True, default='국밥', max_length=10, verbose_name='음식 카테고리 중형')),
                ('dining_food_cate_1', models.CharField(blank=True, default='떡볶이', max_length=10, verbose_name='음식 카테고리1')),
                ('dining_food_cate_2', models.CharField(blank=True, default='라면', max_length=10, verbose_name='음식 카테고리2')),
                ('information', models.CharField(blank=True, default=None, max_length=200, verbose_name='가게 정보')),
                ('isParking', models.BooleanField(default=False, verbose_name='주차 가능 여부')),
                ('isValet', models.BooleanField(default=False, verbose_name='발렛파킹 가능 여부')),
                ('isPet', models.BooleanField(default=False, verbose_name='반려동물 동반 가능 여부')),
                ('isPackaging', models.BooleanField(default=False, verbose_name='포장 가능 여부')),
                ('isReservation', models.BooleanField(default=False, verbose_name='예약 가능 여부')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='주소')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='전화번호')),
                ('menu1', models.CharField(blank=True, max_length=20, verbose_name='대표메뉴1')),
                ('price1', models.CharField(blank=True, max_length=10, null=True, verbose_name='대표메뉴1 가격')),
                ('menu2', models.CharField(blank=True, max_length=20, verbose_name='대표메뉴2')),
                ('price2', models.CharField(blank=True, max_length=10, null=True, verbose_name='대표메뉴2 가격')),
                ('menu_url', models.URLField(blank=True, default='', verbose_name='메뉴 URL')),
                ('diningcode_Star', models.FloatField(blank=True, default=None, null=True, verbose_name='다이닝코드별점')),
                ('diningcode_Score', models.IntegerField(blank=True, default=None, null=True, verbose_name='다이닝코드점수')),
                ('comment', models.IntegerField(blank=True, default=None, null=True, verbose_name='댓글수')),
                ('comment_weight', models.FloatField(blank=True, default=None, null=True, verbose_name='댓글수 가중치')),
                ('rank_score', models.FloatField(blank=True, default=None, null=True, verbose_name='랭킹점수')),
                ('mon_business', models.CharField(blank=True, default='휴무일', max_length=20, null=True, verbose_name='월요일 영업시간')),
                ('mon_breaktime', models.CharField(blank=True, max_length=20, null=True, verbose_name='월요일 브레이크타임')),
                ('tues_business', models.CharField(blank=True, default='휴무일', max_length=20, null=True, verbose_name='화요일 영업시간')),
                ('tues_breaktime', models.CharField(blank=True, max_length=20, null=True, verbose_name='화요일 브레이크타임')),
                ('wed_business', models.CharField(blank=True, default='휴무일', max_length=20, null=True, verbose_name='수요일 영업시간')),
                ('wed_breaktime', models.CharField(blank=True, max_length=20, null=True, verbose_name='수요일 브레이크타임')),
                ('thurs_business', models.CharField(blank=True, default='휴무일', max_length=20, null=True, verbose_name='목요일 영업시간')),
                ('thurs_breaktime', models.CharField(blank=True, max_length=20, null=True, verbose_name='목요일 브레이크타임')),
                ('fri_business', models.CharField(blank=True, default='휴무일', max_length=20, null=True, verbose_name='금요일 영업시간')),
                ('fri_breaktime', models.CharField(blank=True, max_length=20, null=True, verbose_name='금요일 브레이크타임')),
                ('sat_business', models.CharField(blank=True, default='휴무일', max_length=20, null=True, verbose_name='토요일 영업시간')),
                ('sat_breaktime', models.CharField(blank=True, max_length=20, null=True, verbose_name='토요일 브레이크타임')),
                ('sun_business', models.CharField(blank=True, default='휴무일', max_length=20, null=True, verbose_name='일요일 영업시간')),
                ('sun_breaktime', models.CharField(blank=True, max_length=20, null=True, verbose_name='일요일 브레이크타임')),
                ('latitude', models.FloatField(blank=True, default='37.5445023983984', verbose_name='위치 위도')),
                ('longitude', models.FloatField(blank=True, default='127.056090471223', verbose_name='위치 경도')),
                ('img_file1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지1')),
                ('img_file2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지2')),
                ('closest_parking_name', models.CharField(blank=True, max_length=50, verbose_name='가까운 주차장')),
                ('closest_parking_address', models.CharField(blank=True, max_length=100, verbose_name='가까운 주차장 주소')),
                ('closest_parking_latitude', models.FloatField(blank=True, default='37.5445023983984', verbose_name='가까운주차장 위도')),
                ('closest_parking_longitude', models.FloatField(blank=True, default='127.056090471223', verbose_name='가까운주차장 경도')),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
    ]
