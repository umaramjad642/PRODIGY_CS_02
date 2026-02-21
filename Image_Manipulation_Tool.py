from PIL import Image
import os

def process_image(path, key, mode):
    try:
        img = Image.open(path).convert('RGB')
        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                if mode == 'e':
                    # Encryption: Add key to each pixel
                    pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
                else:
                    # Decryption: Subtract key from each pixel
                    pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        # Save as PNG to avoid compression artifacts that break decryption
        output_name = "encrypted_image.png" if mode == 'e' else "decrypted_image.png"
        img.save(output_name)
        print(f"\n[+] Success! Image saved as: {output_name}")

    except Exception as e:
        print(f"\n[!] Error: {e}")

print("--- Prodigy Tech: Image Encryption Tool ---")

while True:
    choice = input("\nType 'E' to Encrypt, 'D' to Decrypt, or 'Q' to Quit: ").lower()

    if choice == 'q':
        print("Exiting tool. Goodbye!")
        break
    
    if choice in ['e', 'd']:
        img_path = input("Enter the image file path: ")
        
        # Check if file exists before proceeding
        if not os.path.exists(img_path):
            print("[!] Error: File not found. Please check the path.")
            continue

        try:
            shift_key = int(input("Enter encryption key (integer): "))
            process_image(img_path, shift_key, choice)
        except ValueError:
            print("[!] Error: Key must be a valid integer.")
    else:
        print("[!] Invalid selection. Please use E, D, or Q.")