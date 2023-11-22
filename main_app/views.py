from django.shortcuts import render

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def restaurants_index(request):
  return render(request, 'restaurants/index.html', {
    'restaurants' : restaurants
  })