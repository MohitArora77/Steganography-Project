from PIL import Image

# Function to encode a message into an image
def encode_message(image_path, message):
    image = Image.open(image_path)
    encoded_image = image.copy()
    
    message += "\0"  # Append a null character to indicate end of message
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    pixels = list(encoded_image.getdata())
    
    if len(binary_message) > len(pixels) * 3:
        raise ValueError("Message is too long to encode in this image.")
    
    new_pixels = []
    binary_index = 0
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Modify the least significant bit of each RGB channel
            if binary_index < len(binary_message):
                new_pixel[i] = (new_pixel[i] & 0xFE) | int(binary_message[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))
    
    encoded_image.putdata(new_pixels)
    encoded_image.save('encoded_image.png')
    print("Message encoded successfully.")

# Function to decode a message from an image
def decode_message(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    
    binary_message = ""
    for pixel in pixels:
        for i in range(3):
            binary_message += str(pixel[i] & 1)
    
    message_chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''.join(chr(int(char, 2)) for char in message_chars)
    
    decoded_message = message.split("\0", 1)[0]  # Extract message before null terminator
    return decoded_message
