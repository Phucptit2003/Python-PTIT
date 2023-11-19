from PIL import Image, ImageDraw
import time

heart_image_path = "C:/Users/phucl/Downloads/bb.jpg"
output_path = "C:/Users/phucl/Downloads/bb.gif"

# Đọc hình ảnh trái tim
heart_image = Image.open(heart_image_path)

# Kích thước trái tim ban đầu
original_width, original_height = heart_image.size

# Số frame và tỉ lệ thu nhỏ
num_frames = 10
scale_factor = 0.9

# Kích thước của hình ảnh mới
new_width = original_width
new_height = original_height

# Tạo danh sách frame
frames = []

# Tạo frame cho mỗi frame
for i in range(num_frames):
    # Tạo hình ảnh mới với kích thước của frame hiện tại
    new_image = Image.new("RGB", (new_width, new_height))

    # Tạo đối tượng vẽ cho frame
    draw = ImageDraw.Draw(new_image)

    # Tính toán vị trí và kích thước cho frame hiện tại
    x = (new_width - original_width) // 2
    y = (new_height - original_height) // 2

    # Thay đổi kích thước trái tim cho frame hiện tại
    current_heart_image = heart_image.resize((new_width, new_height))

    # Vẽ trái tim lên frame
    new_image.paste(current_heart_image, (x, y))

    # Thêm frame vào danh sách frames
    frames.append(new_image)

    # Cập nhật kích thước cho frame tiếp theo
    new_width = int(new_width * scale_factor)
    new_height = int(new_height * scale_factor)

# Đảo ngược danh sách frames để tạo hiệu ứng lặp lại
frames += frames[::-1]

# Lưu thành file GIF
frames[0].save(output_path, format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)

# Hiển thị file GIF
frames[0].show()
