
# Complete project details at https://RandomNerdTutorials.com

def web_page():
  if led5.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  
  led5_on = request.find('/?led5=on')
  led5_off = request.find('/?led5=off')
  if led5_on == 6:
    print('LED 5 ON')
    led5.value(1)
  if led5_off == 6:
    print('LED 5 OFF')
    led5.value(0)
    
  led4_on = request.find('/?led4=on')
  led4_off = request.find('/?led4=off')
  if led4_on == 6:
    print('LED 4 ON')
    led4.value(1)
  if led4_off == 6:
    print('LED 4 OFF')
    led4.value(0)
    
  led0_on = request.find('/?led0=on')
  led0_off = request.find('/?led0=off')
  
  if led0_on == 6:
    print('LED 0 ON')
    led0.value(1)
  if led0_off == 6:
    print('LED 0 OFF')
    led0.value(0)
    
  led2_on = request.find('/?led2=on')
  led2_off = request.find('/?led2=off')
    
  if led2_on == 6:
    print('LED 2 ON')
    led2.value(1)
  if led2_off == 6:
    print('LED 2 OFF')
    led2.value(0)
    
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
