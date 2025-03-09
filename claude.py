import tkinter as tk
from tkinter import messagebox, ttk, font
from PIL import Image, ImageTk
import requests
import json
from datetime import datetime
import os
import io
import math

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Weather App")
        self.root.geometry("900x750")  # Further increased window size
        self.root.resizable(True, True)  # Allow resizing for better adaptability
        
        # Set background color - dark mode inspired
        self.root.configure(bg="#1e1e2e")
        
        # Set a modern theme
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles with modern colors
        style.configure('TFrame', background='#1e1e2e')
        style.configure('TButton', font=('Helvetica', 12, 'bold'), background='#7f5af0', foreground='white')
        style.configure('TLabel', background='#1e1e2e', font=('Helvetica', 12), foreground='#fffffe')
        style.configure('TEntry', font=('Helvetica', 12))
        
        # Configure button styles
        style.map('TButton', 
            background=[('active', '#6247aa')],
            foreground=[('active', 'white')])
        
        # Configure entry style
        style.configure('TEntry', 
            fieldbackground='#2b2c40', 
            foreground='#fffffe',
            insertcolor='#fffffe',
            borderwidth=0)
        
        # Configure separator style
        style.configure('TSeparator', background='#6c757d')
        
        self.api_key = "007b06039a33b6582515d280ad31c35b"
        if not self.api_key:
            raise ValueError("API key not found. Please set the OPENWEATHER_API_KEY environment variable.")
        
        # Create scrollable canvas for the entire content
        self.canvas = tk.Canvas(root, bg="#1e1e2e", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Create main container frame to organize content
        self.main_container = tk.Frame(self.canvas, bg="#1e1e2e")
        self.canvas_window = self.canvas.create_window((0, 0), window=self.main_container, anchor="nw")
        
        # Configure canvas scrolling
        self.main_container.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        
        # Create header frame
        self.header_frame = tk.Frame(self.main_container, pady=15, bg="#1e1e2e")
        self.header_frame.pack(fill="x")
        
        # App title
        self.app_title = tk.Label(
            self.header_frame, 
            text="WEATHER FORECAST", 
            font=("Helvetica", 22, "bold"), 
            bg="#1e1e2e", 
            fg="#fffffe"
        )
        self.app_title.pack()
        
        # Create frame for search with rounded corners effect
        self.search_frame = tk.Frame(self.main_container, pady=10, padx=20, bg="#1e1e2e")
        self.search_frame.pack(fill="x")
        
        # Search container with border radius effect
        self.search_container = tk.Frame(
            self.search_frame, 
            bg="#2b2c40", 
            padx=15, 
            pady=15,
            highlightbackground="#7f5af0",
            highlightthickness=1
        )
        self.search_container.pack(fill="x")
        
        # Create entry for city name
        self.city_label = tk.Label(
            self.search_container, 
            text="Enter city name:", 
            font=("Helvetica", 12), 
            bg="#2b2c40", 
            fg="#94a1b2"
        )
        self.city_label.pack(side="left", padx=10)
        
        # Custom entry with modern styling
        self.city_entry = tk.Entry(
            self.search_container, 
            font=("Helvetica", 12), 
            width=25,
            bg="#2b2c40",
            fg="#fffffe",
            insertbackground="#fffffe",  # Cursor color
            relief=tk.FLAT,
            highlightbackground="#7f5af0",
            highlightthickness=1
        )
        self.city_entry.pack(side="left", padx=10)
        self.city_entry.bind("<Return>", self.get_weather)
        
        # Create search button with modern styling
        self.search_button = tk.Button(
            self.search_container, 
            text="Get Weather", 
            font=("Helvetica", 12, "bold"), 
            command=self.get_weather,
            bg="#7f5af0",  # Modern purple background
            fg="#fffffe",  # White text
            activebackground="#6247aa",  # Darker purple when clicked
            activeforeground="#fffffe",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"  # Hand cursor on hover
        )
        self.search_button.pack(side="left", padx=10)
        
        # Create main content frame
        self.content_frame = tk.Frame(self.main_container, pady=10, bg="#1e1e2e")
        self.content_frame.pack(fill="both", expand=True, padx=20)
        
        # Create weather info display with modern card design
        self.weather_frame = tk.Frame(
            self.content_frame, 
            bg="#2b2c40", 
            padx=30, 
            pady=20
        )
        self.weather_frame.pack(fill="both", expand=True, pady=10)
        
        # Add shadow effect to the weather frame
        self.weather_frame.config(
            highlightbackground="#7f5af0", 
            highlightthickness=2
        )
        
        # City name and date
        self.location_label = tk.Label(
            self.weather_frame, 
            text="", 
            font=("Helvetica", 24, "bold"), 
            bg="#2b2c40", 
            fg="#fffffe",
            wraplength=800  # Allow text to wrap if too long
        )
        self.location_label.pack(pady=(10, 5))
        
        self.date_label = tk.Label(
            self.weather_frame, 
            text="", 
            font=("Helvetica", 12), 
            bg="#2b2c40", 
            fg="#94a1b2",
            wraplength=800  # Allow text to wrap if too long
        )
        self.date_label.pack(pady=5)
        
        # Weather icon
        self.icon_label = tk.Label(self.weather_frame, bg="#2b2c40")
        self.icon_label.pack(pady=10)
        
        # Current weather
        self.weather_main_label = tk.Label(
            self.weather_frame, 
            text="", 
            font=("Helvetica", 18, "bold"), 
            bg="#2b2c40", 
            fg="#fffffe",
            wraplength=800  # Allow text to wrap if too long
        )
        self.weather_main_label.pack(pady=5)
        
        self.temperature_label = tk.Label(
            self.weather_frame, 
            text="", 
            font=("Helvetica", 36, "bold"), 
            bg="#2b2c40", 
            fg="#7f5af0"
        )
        self.temperature_label.pack(pady=5)
        
        # Horizontal separator with modern styling
        separator = ttk.Separator(self.weather_frame, orient='horizontal')
        separator.pack(fill='x', pady=20)
        
        # Details frame with grid layout for better organization
        self.details_frame = tk.Frame(self.weather_frame, bg="#2b2c40")
        self.details_frame.pack(fill="both", expand=True, pady=10)
        
        # Create a 2x3 grid for weather details
        for i in range(2):
            self.details_frame.columnconfigure(i, weight=1)
            self.details_frame.rowconfigure(i, weight=1)
            
        # Weather detail items with icons (using text symbols for now)
        # First row
        self.feels_like_frame = self.create_detail_item(
            self.details_frame, "🌡️", "Feels like", "", 0, 0
        )
        
        self.humidity_frame = self.create_detail_item(
            self.details_frame, "💧", "Humidity", "", 0, 1
        )
        
        # Second row
        self.pressure_frame = self.create_detail_item(
            self.details_frame, "⏱️", "Pressure", "", 1, 0
        )
        
        self.visibility_frame = self.create_detail_item(
            self.details_frame, "👁️", "Visibility", "", 1, 1
        )
        
        # Additional details frame for wind and clouds
        self.additional_details_frame = tk.Frame(self.weather_frame, bg="#2b2c40")
        self.additional_details_frame.pack(fill="both", expand=True, pady=10)
        
        # Create a 1x2 grid for additional weather details
        for i in range(2):
            self.additional_details_frame.columnconfigure(i, weight=1)
        self.additional_details_frame.rowconfigure(0, weight=1)
        
        # Wind
        self.wind_frame = self.create_detail_item(
            self.additional_details_frame, "💨", "Wind", "", 0, 0
        )
        
        # Cloudiness
        self.clouds_frame = self.create_detail_item(
            self.additional_details_frame, "☁️", "Cloudiness", "", 0, 1
        )
        
        # Status bar with modern styling
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = tk.Label(
            root, 
            textvariable=self.status_var, 
            relief=tk.FLAT, 
            anchor="w", 
            font=("Helvetica", 10),
            bg="#2b2c40",
            fg="#94a1b2",
            padx=10,
            pady=5
        )
        self.status_bar.pack(side="bottom", fill="x")
        
        # Weather icons cache
        self.icon_cache = {}
        
        # Set minimum size to ensure all content is visible
        self.root.update()
        self.root.minsize(800, 700)
    
    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def on_canvas_configure(self, event):
        """When the canvas is resized, resize the window within it too"""
        width = event.width
        self.canvas.itemconfig(self.canvas_window, width=width)
    
    def on_mousewheel(self, event):
        """Handle mousewheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def create_detail_item(self, parent, icon, label_text, value_text, row, column):
        """Create a weather detail item with icon, label and value"""
        frame = tk.Frame(parent, bg="#2b2c40", padx=10, pady=10)
        frame.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        
        # Icon and label in one row
        header_frame = tk.Frame(frame, bg="#2b2c40")
        header_frame.pack(anchor="w")
        
        icon_label = tk.Label(
            header_frame, 
            text=icon, 
            font=("Helvetica", 14), 
            bg="#2b2c40", 
            fg="#94a1b2"
        )
        icon_label.pack(side="left", padx=(0, 5))
        
        text_label = tk.Label(
            header_frame, 
            text=label_text, 
            font=("Helvetica", 12), 
            bg="#2b2c40", 
            fg="#94a1b2"
        )
        text_label.pack(side="left")
        
        # Value in another row
        value_label = tk.Label(
            frame, 
            text=value_text, 
            font=("Helvetica", 14, "bold"), 
            bg="#2b2c40", 
            fg="#fffffe",
            wraplength=300  # Allow text to wrap if too long
        )
        value_label.pack(anchor="w", pady=(5, 0))
        
        return {
            "frame": frame,
            "icon": icon_label,
            "label": text_label,
            "value": value_label
        }
    
    def get_weather(self, event=None):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return
        
        self.status_var.set(f"Fetching weather data for {city}...")
        self.root.update_idletasks()
        
        # API request
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code != 200:
                error_message = data.get('message', 'Unknown error')
                messagebox.showerror("Error", f"Failed to get weather data: {error_message}")
                self.status_var.set("Ready")
                return
            
            # Update UI with weather data
            self.update_weather_ui(data)
            
            # Ensure all content is visible after updating
            self.root.update_idletasks()
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.canvas.yview_moveto(0)  # Scroll to top
            
            self.status_var.set(f"Weather data for {city} retrieved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Ready")
    
    def get_weather_icon(self, icon_code):
        """Fetch weather icon from OpenWeatherMap API"""
        if icon_code in self.icon_cache:
            return self.icon_cache[icon_code]
        
        try:
            url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"  # Using larger icons
            response = requests.get(url)
            
            if response.status_code == 200:
                image_data = response.content
                img = Image.open(io.BytesIO(image_data))
                img = img.resize((120, 120), Image.LANCZOS)  # Larger icon size
                photo_img = ImageTk.PhotoImage(img)
                self.icon_cache[icon_code] = photo_img
                return photo_img
            return None
        except Exception as e:
            print(f"Error fetching weather icon: {e}")
            return None
    
    def update_weather_ui(self, data):
        # Translation dictionary for weather conditions
        translation_dict = {
            "Clear": "صاف",
            "Clouds": "ابری",
            "Rain": "بارانی",
            "Snow": "برفی",
            "Mist": "مه",
            "Fog": "مه غلیظ",
            "Drizzle": "نم نم باران",
            "Thunderstorm": "رعد و برق",
            "Haze": "غبار",
            "Smoke": "دود",
            "Dust": "گرد و غبار",
            "Sand": "شن",
            "Ash": "خاکستر",
            "Squall": "تندباد",
            "Tornado": "گردباد"
        }

        # City name and country
        city_name = data['name']
        country = data['sys']['country']
        self.location_label.config(text=f"{city_name}, {country}")
        
        # Date and time
        timestamp = data['dt']
        date_time = datetime.fromtimestamp(timestamp)
        formatted_date = date_time.strftime("%A, %B %d, %Y %I:%M %p")
        self.date_label.config(text=formatted_date)
        
        # Weather icon
        icon_code = data['weather'][0]['icon']
        icon_img = self.get_weather_icon(icon_code)
        if icon_img:
            self.icon_label.config(image=icon_img)
            self.icon_label.image = icon_img  # Keep a reference
        
        # Weather condition
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        weather_main_persian = translation_dict.get(weather_main, weather_main)
        self.weather_main_label.config(text=f"{weather_main_persian} ({weather_description.capitalize()})")
        
        # Temperature
        temp = data['main']['temp']
        self.temperature_label.config(text=f"{round(temp)}°C")
        
        # Update detail items
        feels_like = data['main']['feels_like']
        self.feels_like_frame["value"].config(text=f"{round(feels_like)}°C")
        
        humidity = data['main']['humidity']
        self.humidity_frame["value"].config(text=f"{humidity}%")
        
        wind_speed = data['wind']['speed']
        wind_direction = data['wind'].get('deg', 0)
        self.wind_frame["value"].config(text=f"{wind_speed} m/s, {self.get_wind_direction(wind_direction)}")
        
        pressure = data['main']['pressure']
        self.pressure_frame["value"].config(text=f"{pressure} hPa")
        
        visibility = data.get('visibility', 0) / 1000  # Convert to km
        self.visibility_frame["value"].config(text=f"{visibility:.1f} km")
        
        cloudiness = data['clouds']['all']
        self.clouds_frame["value"].config(text=f"{cloudiness}%")
        
        # Update UI colors based on weather condition
        self.apply_weather_theme(weather_main, temp)
    
    def apply_weather_theme(self, weather_condition, temperature):
        """Apply theme colors based on weather condition and temperature"""
        # Base colors for dark theme
        bg_color = "#2b2c40"  # Dark background
        card_bg = "#2b2c40"   # Card background
        text_color = "#fffffe"  # White text
        accent_color = "#7f5af0"  # Purple accent
        secondary_text = "#94a1b2"  # Gray text
        
        # Subtle accent color variations based on weather
        if weather_condition == "Clear":
            if temperature > 25:  # Hot sunny day
                accent_color = "#ff8906"  # Orange
            else:  # Cool sunny day
                accent_color = "#7f5af0"  # Purple
        elif weather_condition in ["Clouds", "Mist", "Fog", "Haze"]:
            accent_color = "#2cb67d"  # Teal
        elif weather_condition in ["Rain", "Drizzle", "Thunderstorm"]:
            accent_color = "#3da9fc"  # Blue
        elif weather_condition == "Snow":
            accent_color = "#90b4ce"  # Light blue
        
        # Apply accent color to temperature and border
        self.temperature_label.config(fg=accent_color)
        self.weather_frame.config(highlightbackground=accent_color)
        self.search_container.config(highlightbackground=accent_color)
        self.search_button.config(bg=accent_color, activebackground=self.darken_color(accent_color))
        self.city_entry.config(highlightbackground=accent_color)
    
    def darken_color(self, hex_color, factor=0.8):
        """Darken a hex color by a factor"""
        # Convert hex to RGB
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Darken
        r = max(0, int(r * factor))
        g = max(0, int(g * factor))
        b = max(0, int(b * factor))
        
        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def get_wind_direction(self, degrees):
        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", 
                       "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        index = round(degrees / 22.5) % 16
        return directions[index]

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()