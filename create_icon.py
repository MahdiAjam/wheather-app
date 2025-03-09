from PIL import Image, ImageDraw
import os

def create_weather_icon():
    # Create a 256x256 image with a transparent background
    icon_size = 256
    icon = Image.new('RGBA', (icon_size, icon_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(icon)
    
    # Define colors
    sky_blue = (127, 90, 240)  # Purple to match app theme
    cloud_color = (255, 255, 255, 230)
    sun_color = (255, 137, 6)
    
    # Draw a circle for the sun
    sun_radius = 60
    sun_position = (icon_size // 2 - 40, icon_size // 2 - 20)
    draw.ellipse(
        (
            sun_position[0] - sun_radius,
            sun_position[1] - sun_radius,
            sun_position[0] + sun_radius,
            sun_position[1] + sun_radius
        ),
        fill=sun_color
    )
    
    # Draw clouds
    # First cloud
    cloud_positions = [
        (icon_size // 2 + 20, icon_size // 2 + 20),
        (icon_size // 2 + 50, icon_size // 2 + 10),
        (icon_size // 2 + 80, icon_size // 2 + 30),
        (icon_size // 2 + 60, icon_size // 2 + 50),
        (icon_size // 2 + 30, icon_size // 2 + 45),
        (icon_size // 2 + 10, icon_size // 2 + 30),
    ]
    
    for pos in cloud_positions:
        draw.ellipse(
            (
                pos[0] - 30,
                pos[1] - 20,
                pos[0] + 30,
                pos[1] + 20
            ),
            fill=cloud_color
        )
    
    # Save as ICO file
    icon.save('weather_icon.ico', format='ICO', sizes=[(256, 256)])
    print(f"Icon created: {os.path.abspath('weather_icon.ico')}")

if __name__ == "__main__":
    create_weather_icon() 