from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406354303',
        'name': 'Ghiyas Fazle Mawla Rahmat',
        'class': 'PBP A',
        'project' : 'ChelseaShop'
    }

    return render(request, "main.html", context)
