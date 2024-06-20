from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from restaurant.models import Restaurant
from .forms import QuestionForm
import csv

def restaurant_list(request):
    """
    맛집 데이터 목록 출력
    """
    #입력인자
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #키워드 검색
    # 조회
    restaurant_list = Restaurant.objects.order_by('no')
    if kw:
        restaurant_list = restaurant_list.filter(
            Q(title__icontains=kw) |  # 상호명 검색
            Q(local_category__icontains=kw) |  # 지역 검색
            Q(dining_food_cate_1__icontains=kw)  # 음식카테고리 검색
        ).distinct()

    #페이징 처리
    paginator = Paginator(restaurant_list, 10) #restaurant_list를 페이지네이션
    page_obj = paginator.get_page(page)
    context = {'restaurant_list': page_obj, 'page': page, 'kw':kw} #템플릿에서 사용할 데이터를 context 딕셔너리에 저장
    return render(request, 'restaurant/restaurant_list.html', context)

def restaurant_detail(request, restaurant_no):
    restaurant = get_object_or_404(Restaurant, no=restaurant_no)

    # 이미지 파일 경로를 템플릿으로 전달하기 위해 context에 추가합니다.
    img_urls = []
    if restaurant.img_file1:
        if restaurant.img_file1.url and restaurant.img_file1.storage.exists(restaurant.img_file1.name):
            img_urls.append(restaurant.img_file1.url)
    if restaurant.img_file2:
        if restaurant.img_file2.url and restaurant.img_file2.storage.exists(restaurant.img_file2.name):
            img_urls.append(restaurant.img_file2.url)
    # 이미지가 없는 경우 처리
    if not img_urls:
        img_urls = None  # None으로 설정하여 템플릿에서 처리할 수 있도록 합니다
    context = {'restaurant': restaurant, 'img_urls': img_urls}
    return render(request, 'restaurant/restaurant_detail.html', context)

def restaurant_create(request):
    """
    맛집 데이터 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST) #등록폼 개설
        if form.is_valid():
            restaurant = form.save(commit=True)
            restaurant.save()
            return redirect('restaurant:restaurant_list')
        else:
            print(form.errors)  # 폼 에러를 출력하여 디버깅
    else:
        form = QuestionForm() #사용자가 폼을 제출하지 않은 경우, 빈 폼을 생성합니다.
    context = {'form': form}
    return render(request, 'restaurant/restaurant_form.html', context)
