from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('6070f9abd8ee8d257d73d437c9bfff4e')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Ghana,Gh')
w = observation.weather

print(w.detailed_status)  
print(w.wind())                  
print(w.humidity)                
print(w.temperature('celsius') ) 
print(w.rain)                    
print(w.heat_index)             
print(w.clouds)                  

