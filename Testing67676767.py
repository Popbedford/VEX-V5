def advanced_color_detection():
    while True:
        # Check if an object is detected
        if optical_sensor.is_near_object():
            hue = optical_sensor.hue()
            saturation = optical_sensor.saturation()
            brightness = optical_sensor.brightness()
           
            # Only detect colors if saturation is high enough
            if saturation > 30 and brightness > 20:
                color_name = get_color_name(hue)
                brain.screen.print_at("Color: {}".format(color_name), 10, 50)
                brain.screen.print_at("Confidence: High", 10, 70)
            else:
                brain.screen.print_at("Color: Unclear    ", 10, 50)
                brain.screen.print_at("Confidence: Low ", 10, 70)
        else:
            brain.screen.print_at("No object detected", 10, 50)
            brain.screen.print_at("                  ", 10, 70)
       
        wait(100, MSEC)
def object_sorting():
    # Turn on the optical sensor LED for better detection
    optical_sensor.set_light(LedState.ON)
    optical_sensor.set_light_power(100, PERCENT)
   
    while True:
        if optical_sensor.is_near_object():
            hue = optical_sensor.hue()
           
            brain.screen.print_at("Object detected!", 10, 50)
            brain.screen.print_at("Hue: {:.1f}".format(hue), 10, 70)
           
            # Sort based on color
            if 0 <= hue < 60:  # Red/Orange/Yellow
                brain.screen.print_at("Sort to BIN A", 10, 90)
                # Add motor code to sort to bin A
            elif 60 <= hue < 180:  # Green
                brain.screen.print_at("Sort to BIN B", 10, 90)
                # Add motor code to sort to bin B
            else:  # Blue/Purple
                brain.screen.print_at("Sort to BIN C", 10, 90)
                # Add motor code to sort to bin C
        else:
            brain.screen.print_at("Waiting for object...", 10, 50)
            brain.screen.print_at("                     ", 10, 70)
            brain.screen.print_at("                     ", 10, 90)
       
        wait(100, MSEC)
