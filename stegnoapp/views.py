from django.shortcuts import render, redirect
from django.contrib import messages
from .models import StegoImage
from .forms import StegoImageForm
from .steganography import encode_message, decode_message

def steganography_view(request):
    decoded_message = None
    if request.method == 'POST':
        form = StegoImageForm(request.POST, request.FILES)
        if form.is_valid():
            stego_image = form.save()
            image_path = stego_image.image.path
            message = form.cleaned_data.get('message', '')
            
            if 'encode' in request.POST:  # Encoding logic
                if message:
                    try:
                        encode_message(image_path, message)
                        stego_image.encoded_message = message
                        stego_image.save()
                        messages.success(request, "Image uploaded and encoded successfully!")
                    except Exception as e:
                        messages.error(request, f"Error encoding message: {e}")
                else:
                    messages.warning(request, "No message provided for encoding.")
            
            elif 'decode' in request.POST:  # Decoding logic
                try:
                    decoded_message = decode_message(image_path)
                    messages.success(request, f"Decoded message: {decoded_message}")
                except Exception as e:
                    messages.error(request, f"Error decoding message: {e}")
    else:
        form = StegoImageForm()
    
    return render(request, 'index.html', {'form': form, 'decoded_message': decoded_message})

