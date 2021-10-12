
# Complete project details at https://RandomNerdTutorials.com


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
    
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.close()
