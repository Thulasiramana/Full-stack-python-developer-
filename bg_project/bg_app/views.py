from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from rembg import remove
from PIL import Image
import os
from django.conf import settings 

def upload_file(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        
        # Save the image using FileSystemStorage
        fs = FileSystemStorage(location = settings.MEDIA_ROOT)
        filename = fs.save(image.name, image)
        image_path = fs.path(filename)
        
        # Process the image to remove the background using rembg
        img = Image.open(image_path)
        output = remove(img)
        
        # Save the processed image
        output_filename = f"bg_removed_{filename}.png"
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
        output.save(output_path)

        # Get the URL for the processed image
        image_url = fs.url(output_filename)
        
        # Redirect to the view image page
        return redirect('view_image', image_url=image_url)
    
    return render(request, 'main.html')

def view_image(request, image_url):
    return render(request, 'view_image.html', {'image_url': image_url})

def viewmain(request):
    return render(request, 'main.html')