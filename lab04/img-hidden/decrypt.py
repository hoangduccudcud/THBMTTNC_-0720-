import sys
from PIL import Image

def decode_image(encoded_image_path):
    try:
        img = Image.open(encoded_image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return ""
    
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            # Lấy bit cuối cùng của mỗi kênh màu
            for color_channel in range(3):  # RGB
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi binary_message thành thông điệp
    message = ""
    for i in range(0, len(binary_message), 8):
        char_bits = binary_message[i:i+8]
        if char_bits == '11111110':  # Check for the message termination marker
            break
        char = chr(int(char_bits, 2))
        message += char
    
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    
    if decoded_message:
        print("Decoded message:", decoded_message)
    else:
        print("No message decoded or error occurred.")

if __name__ == "__main__":
    main()
