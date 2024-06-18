from django.db import models

class Restaurant(models.Model):
    # restaurant_id = models.BigAutoField(primary_key=True)  # 레스토랑 ID, 자동 생성
    no = models.IntegerField(verbose_name="no", primary_key=True)
    title = models.CharField(max_length=30, verbose_name="상호명")  # 음식카테고리, 로컬카테고리, 상호명은 필수
    local_category = models.CharField(max_length=20, verbose_name="지역")
    food_category_1st = models.CharField(max_length=10, verbose_name="음식 카테고리 대형", default='한식', blank=True)
    food_category_2nd = models.CharField(max_length=10, verbose_name="음식 카테고리 중형", default='국밥', blank=True)
    dining_food_cate_1 = models.CharField(max_length=10, verbose_name="음식 카테고리1", default='떡볶이',blank=True)
    dining_food_cate_2 = models.CharField(max_length=10, verbose_name="음식 카테고리2",default='라면',blank=True)
    information = models.CharField(max_length=200, verbose_name="가게 정보", default=None, blank=True)
    isParking = models.BooleanField(default=False, verbose_name="주차 가능 여부")
    isValet = models.BooleanField(default=False, verbose_name="발렛파킹 가능 여부")
    isPet = models.BooleanField(default=False, verbose_name="반려동물 동반 가능 여부")
    isPackaging = models.BooleanField(default=False, verbose_name="포장 가능 여부")
    isReservation = models.BooleanField(default=False, verbose_name="예약 가능 여부")
    address = models.CharField(max_length=100, verbose_name="주소", blank=True)
    telephone = models.CharField(max_length=20, verbose_name="전화번호", blank=True, null=True)
    menu1 = models.CharField(max_length=20, verbose_name="대표메뉴1", blank=True)
    price1 = models.CharField(max_length=10, verbose_name="대표메뉴1 가격", blank=True, null=True)
    menu2 = models.CharField(max_length=20, verbose_name="대표메뉴2", blank=True)
    price2 = models.CharField(max_length=10, verbose_name="대표메뉴2 가격", blank=True, null=True)
    menu_url = models.URLField(verbose_name="메뉴 URL", default='', blank=True)
    diningcode_Star = models.FloatField(verbose_name="다이닝코드별점", default=None, null=True, blank=True)
    diningcode_Score = models.IntegerField(verbose_name="다이닝코드점수", default=None, null=True, blank=True)
    comment = models.IntegerField(verbose_name="댓글수", default=None, null=True, blank=True)
    comment_weight = models.FloatField(verbose_name="댓글수 가중치",default=None, null=True, blank=True)
    rank_score = models.FloatField(verbose_name="랭킹점수",default=None, null=True, blank=True)
    mon_business = models.CharField(max_length=20, verbose_name="월요일 영업시간", null=True, default='휴무일', blank=True)
    mon_breaktime = models.CharField(max_length=20, verbose_name="월요일 브레이크타임", null=True, blank=True)
    tues_business = models.CharField(max_length=20, verbose_name="화요일 영업시간", null=True, default='휴무일', blank=True)
    tues_breaktime = models.CharField(max_length=20, verbose_name="화요일 브레이크타임", null=True, blank=True)
    wed_business = models.CharField(max_length=20, verbose_name="수요일 영업시간", null=True, default='휴무일', blank=True)
    wed_breaktime = models.CharField(max_length=20, verbose_name="수요일 브레이크타임", null=True, blank=True)
    thurs_business = models.CharField(max_length=20, verbose_name="목요일 영업시간", null=True, default='휴무일', blank=True)
    thurs_breaktime = models.CharField(max_length=20, verbose_name="목요일 브레이크타임", null=True, blank=True)
    fri_business = models.CharField(max_length=20, verbose_name="금요일 영업시간", null=True, default='휴무일', blank=True)
    fri_breaktime = models.CharField(max_length=20, verbose_name="금요일 브레이크타임", null=True, blank=True)
    sat_business = models.CharField(max_length=20, verbose_name="토요일 영업시간", null=True, default='휴무일', blank=True)
    sat_breaktime = models.CharField(max_length=20, verbose_name="토요일 브레이크타임", null=True, blank=True)
    sun_business = models.CharField(max_length=20, verbose_name="일요일 영업시간", null=True, default='휴무일', blank=True)
    sun_breaktime = models.CharField(max_length=20, verbose_name="일요일 브레이크타임", null=True, blank=True)
    latitude = models.FloatField(verbose_name="위치 위도", null=False, default='37.5445023983984',blank=True)
    longitude = models.FloatField(verbose_name="위치 경도", null=False, default='127.056090471223', blank=True)
    img_file1 = models.ImageField(null=True, upload_to="", blank=True, verbose_name="이미지1")
    img_file2 = models.ImageField(null=True, upload_to="", blank=True, verbose_name="이미지2")
    closest_parking_name = models.CharField(max_length=50, verbose_name="가까운 주차장", blank=True)
    closest_parking_address = models.CharField(max_length=100, verbose_name="가까운 주차장 주소", blank=True)
    closest_parking_latitude = models.FloatField(verbose_name="가까운주차장 위도", null=False, default='37.5445023983984', blank=True)
    closest_parking_longitude = models.FloatField(verbose_name="가까운주차장 경도", null=False, default='127.056090471223', blank=True)

    class Meta:
        db_table = 'restaurant'  # 테이블 이름 지정


    def __str__(self):
        return self.title


        #객체를 문자열로 변환할 때 사용되는 메서드입니다.
        #예를 들어, Django의 admin 페이지에서 객체가 표시되는 방식을 정의합니다.
        #이 경우, 객체의 제목(title)을 문자열로 반환합니다.





