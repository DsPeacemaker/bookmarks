from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        # форма отправлена
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # данные в форме валидны
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # назначить текушего пользователя элементу
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            # Перенаправить к представлению детальной
            # информации о только что созданном элементе
            return redirect(new_image.get_absolute_url())
    else:
        # скомпоновать форму с данными,
        # информации о только что созданном элементе
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})
