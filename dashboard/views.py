from django.core.paginator import Paginator
from django.shortcuts import render
from dashboard.models import Course  # Adjust the path if necessary

def course_list(request):
    # Get all courses, ordered by `course_id` (newest first)
    course_queryset = Course.objects.all().order_by('-course_id')

    # Paginate the courses (e.g., 10 courses per page)
    paginator = Paginator(course_queryset, 9)  # 10 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the paginated courses to the template
    return render(request, 'main.html', {'page_obj': page_obj})
